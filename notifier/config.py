""" config class """
from typing import Optional

import yaml


class Config:
    """config class"""

    def __init__(self):
        self.config_file_name = "config.yaml"
        self.config = self.__read_config(self.config_file_name)

    def get(self, key: str) -> Optional[str]:
        """Get value from config
        Args:
            key (str): key of config
        Returns:
            Optional[str]: value of config
        """
        return self.config.get(key)

    def get_config(self) -> dict:
        """Get config
        Returns:
            dict: config
        """
        return self.config

    def set(self, key: str, value: str) -> None:
        """Set value to config
        Args:
            key (str): key of config
            value (str): value of config
        """
        self.config[key] = value

    def __read_config(self) -> dict:
        """Read config from file
        Returns:
            dict: config
        """
        with open(self.config_file_name, "r", encoding="utf-8") as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
        return config


config_file = Config()
