""" new objects for news_notifier """
from time import sleep

from notifier.bot.telegram_bot import TelegramBot
from notifier.config import config_file
from notifier.news_api_handler import NewsApiHandler
from notifier.news_formatter import NewsFormatter


class NewsNotificator:
    """news notificator object"""

    def __init__(self, bot: TelegramBot) -> None:
        """Initilize news notificator
        Args:
            bot (TelegramBot): telegram bot
        """
        self.bot = bot
        self.api_handler = NewsApiHandler()

    def get_news(self) -> list:
        """Get news from news api
        Returns:
            list: news list
        """
        news = self.api_handler.get_news()
        return news

    def notify_news(self, news: list) -> None:
        """Notify news to telegram bot
        Args:
            news (list): news list
        """
        formatter = NewsFormatter()
        messages = formatter.format_news_to_telegram_message(news)
        for message in messages:
            self.bot.send_message(message)

    def modify_settings(self, args: dict) -> None:
        """Modify news settings.
        Args:
            args (dict): args of news
        """
        self.api_handler.set_args(args)
        print(self.api_handler.args)

    def say_hi(self, update: dict) -> None:
        """Say hi to user
        Args:
            update (dict): update from telegram bot
        """
        user = update["message"]["chat"]["first_name"]
        self.bot.send_message(f"Hello {user} the news are:")

    def news_process(self) -> None:
        """Process news, get news and notify news"""
        news = self.get_news()
        self.notify_news(news)

    def message_handler(self, update: dict) -> None:
        """Handle message from telegram bot
        Args:
            update (dict): update from telegram bot
        """
        message = update["message"]["text"]
        if message.strip() == config_file.get("COMMAND_ACTIVATE"):
            self.say_hi(update)
            self.news_process()
        elif message.strip() == config_file.get("COMMAND_HELP"):
            self.bot.send_message(self.get_help())

    def get_help(self) -> str:
        """Get help for bot
        Returns:
            str: help message
        """
        help_message = f"""{config_file.get('COMMAND_HELP')} : Show this message
        {config_file.get('COMMAND_ACTIVATE')} : Start news process
        """
        return help_message

    def suscribe_updates(self) -> None:
        """Suscribe to updates from telegram bot"""
        polling = True
        sleep_time = 1
        last_id = 0
        while polling:
            result_update = self.bot.get_last_update(last_id)
            if result_update:
                last_id = result_update[-1]["update_id"]
                self.message_handler(result_update[-1])
            sleep(sleep_time)
