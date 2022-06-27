""" bot class telegram """
import requests

from bot.bot_interface import BotInterface


class TelegramBot(BotInterface):
    """Telegram bot class."""

    def __init__(self, bot_token: str, chat_id: str, name: str = "Telegram Bot"):
        """Initialize bot.
        Args:
            bot_token (str): token of bot
            chat_id (str): id of chat
            name (str, optional): name of bot. Defaults to "Telegram Bot".
        """
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.name = name
        self.apli_telegram_url = f"https://api.telegram.org/bot{self.bot_token}"

    def get_name(self) -> str:
        """Get name of bot
        Returns:
            str: name of bot
        """
        return self.name

    def set_name(self, name: str):
        """Set name of bot.
        Args:
            name (str): name of bot
        """
        self.name = name

    def send_message(self, message: str) -> dict:
        """Send message to chat
        Args:
            message (str): message to send
        Returns:
            dict:   response from telegram
        """
        url = f"{self.apli_telegram_url}/sendMessage?chat_id={self.chat_id}&text={message}"
        response = requests.get(url)
        return response.json()

    def send_image(self, url_image: str) -> dict:
        """Send image to chat
        Args:
            url_image (str): url of image
        Returns:
            dict: response from telegram
        """
        url = f"{self.apli_telegram_url}/sendPhoto?chat_id={self.chat_id}&photo={url_image}"
        response = requests.get(url)
        return response.json()

    def send_image_from_file(self, image_path: str) -> dict:
        """Send image to chat
        Args:
            image_path (str): path of image
        Returns:
            dict: response from telegram
        """
        url = f"{self.apli_telegram_url}/sendPhoto?chat_id={self.chat_id}"
        files = {"photo": open(image_path, "rb")}
        response = requests.post(url, files=files)
        return response.json()
