""" new objects for news_notifier """
from news_notifier.bot.telegram_bot import TelegramBot
from news_notifier.config import default_settings
from news_notifier.news_api_handler import NewsApiHandler
from news_notifier.news_formatter import NewsFormatter


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

    def get_help(self) -> str:
        """Get help message
        Returns:
            str: help message
        """
        return f"""
            {default_settings["COMMAND_TO_ACTIVATE"]} - start news process
            {default_settings["COMMAND_SETTINGS"]} - set news settings
                example: /{default_settings["COMMAND_SETTINGS"]} country=us category=general
            {default_settings["COMMAND_SETTINGS_DEFAULT"]} - set default news settings
            {default_settings["COMMAND_HELP"]} - get help
            Available options:
            - category - get news by category
            can be: 
                business, entertainment, general, health, science, sports, technology
            - country - get news by country
                some examples: 
                ar, au, br, ca, co, fr, jp, mx, nz, us, ve https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
            - page - get news by page
            - language - get news by language
            - page_size - get news by page size
            """.replace(
            "\t\t", ""
        )

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
        print(message)
        if message.strip() == default_settings["COMMAND_TO_ACTIVATE"]:
            print("Start news process")
            self.say_hi(update)
            # self.news_process()
            print("End news process")
        elif default_settings["COMMAND_SETTINGS"] in message:
            message_list = message.split(" ")
            if len(message_list) > 1:
                args_list = [item.split("=") for item in message_list[1:]]
                args = {item[0]: item[1] for item in args_list}
                username = update["message"]["chat"]["username"]
                args = {**args, "username": username}
                self.modify_settings(args)
            else:
                self.bot.send_message(
                    f"The format of command {default_settings['COMMAND_SETTINGS']} is: {default_settings['COMMAND_SETTINGS']} <option>=<value>"
                )
        elif message.strip() == default_settings["COMMAND_SETTINGS_DEFAULT"]:
            print("Set default settings")
            self.api_handler.set_default_args()
        elif message.strip() == default_settings["COMMAND_HELP"]:
            print(self.get_help())
            self.bot.send_message_without_link_preview(self.get_help())
