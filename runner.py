""" runner """
import argparse

from news_notifier.bot.telegram_bot import TelegramBot
from news_notifier.news_notificator import NewsNotificator

parser = argparse.ArgumentParser()
parser.add_argument(
    "--execution-type",
    type=str,
    required=False,
    default="telegram",
    help="Type of execution could be 'handler' to keep pending of message or default",
)
parser.add_argument("--bot-token", type=str, required=True, help="Token of bot")
parser.add_argument("--chat-id", type=str, required=True, help="Id of chat")
parser.add_argument("--message", type=str, required=False, help="Message to send")


def run(args: argparse.Namespace):
    """Run news notificator
    Args:
        args (argparse.Namespace): arguments from command line
    """
    bot = TelegramBot(args.bot_token, args.chat_id)
    news_notificator = NewsNotificator(bot)
    if args.execution_type == "handler":
        bot.suscribe_updates(news_notificator.message_handler)
    else:
        news_notificator.news_process()


if __name__ == "__main__":
    args = parser.parse_args()
    run(args)
