""" bot class telegram """
import requests
from notifier.config import config_file

class TelegramBot:
    """Telegram bot class."""

    def __init__(self, bot_token: str, chat_id: str):
        """Initialize bot.
        Args:
            bot_token (str): token of bot
            chat_id (str): id of chat
        """
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.url = f"https://api.telegram.org/bot{self.bot_token}"
        self.function_to_execute = None

    def send_message(self, message: str) -> None:
        """Send message to chat.
        Args:
            message (str): message to send
        """
        params = {"chat_id": self.chat_id, "text": message}
        url = f"{self.url}/sendMessage"
        requests.post(url, params=params)

    def send_message_without_link_preview(self, link: str) -> None:
        """Send link without preview to chat.
        Args:
            link (str): link to send
        """
        params = {
            "chat_id": self.chat_id,
            "disable_web_page_preview": True,
            "text": link,
        }
        url = f"{self.url}/sendMessage"
        requests.post(url, params=params)  # type: ignore

    def get_last_update(self, last_id: int) -> dict:
        """Get last update from telegram chat.
        Args:
            last_id (int): id of last update

        Returns:
            dict: last update
        """
        offset = last_id + 1
        url = f"{self.url}/getUpdates?offset={offset}"
        response = requests.get(url)
        return response.json()["result"]

