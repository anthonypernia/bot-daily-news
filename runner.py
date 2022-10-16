""" runner """
import argparse
from ast import arg

from notifier.bot.telegram_bot import TelegramBot
from notifier.news_notificator import NewsNotificator

parser = argparse.ArgumentParser()
parser.add_argument(
    "--handle-messages",
    type=int,
    required=False,
    default=0,
    help="Type of execution could be '1' to keep pending of message or 0 to send news",
)
parser.add_argument("--bot-token", type=str, required=True, help="Token of bot")
parser.add_argument("--chat-id", type=str, required=True, help="Id of chat")


def run(args: argparse.Namespace):
    """Run news notificator
    Args:
        args (argparse.Namespace): arguments from command line
    """
    bot = TelegramBot(args.bot_token, args.chat_id)
    news_notificator = NewsNotificator(bot)
    if args.handle_messages in ['1', 1]:
        news_notificator.suscribe_updates()
    else:
        news_notificator.news_process()


if __name__ == "__main__":
    args = parser.parse_args()
    run(args)
