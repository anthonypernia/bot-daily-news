""" Interface for the bot. """
from abc import ABC, abstractmethod


class BotInterface(ABC):
    """Telegram bot interface."""

    @abstractmethod
    def get_name(self):
        """Get name of bot."""

    @abstractmethod
    def set_name(self, name: str):
        """Set name of bot.
        Args:
            name (str): name of bot
        """

    @abstractmethod
    def send_message(self, message: str):
        """Send message to chat.
        Args:
            message (str): message to send
        """

    @abstractmethod
    def send_image(self, url_image: str):
        """Send image to chat.
        Args:
            url_image (str): url of image
        """

    @abstractmethod
    def send_image_from_file(self, image_path: str):
        """Send image to chat.
        Args:
            image_path (str): path of image local
        """
