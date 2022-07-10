""" news api handler """
import requests

from news_notifier.config import default_settings


class NewsApiHandler:
    """object to get data from api news"""

    def __init__(self) -> None:
        """Initialize object"""
        self.url = default_settings["URL_NEWS"]
        self.api_key = default_settings["API_KEY"]
        self.country = default_settings["COUNTRY"]
        self.page_size = default_settings["PAGE_SIZE"]
        self.language = default_settings["LANGUAGE"]
        self.category = default_settings["CATEGORY"]
        self.set_default_args()

    def set_default_args(self) -> None:
        """Set default args"""
        self.args = {
            "country": self.country,
            "category": self.category,
            "apiKey": self.api_key,
            "pageSize": self.page_size,
            "page": 1,
            "language": self.language,
        }

    def set_args(self, args: dict) -> None:
        """Set args of news
        Args:
            args (dict): args of news
        """
        for key in args:
            if key in self.args:
                self.args[key] = args[key]
        print(self.args)

    def get_news(self) -> list:
        """Get news from API
        Returns:
            list: list of news
        """
        response = requests.get(self.url, params=self.args)  # type: ignore
        return response.json()["articles"]

    def get_news_by_category(self, category: str) -> list:
        """Get news from API by category
        Args:
            category (str): category of news
        Returns:
            list: list of news
        """
        self.args["category"] = category
        return self.get_news()

    def get_news_by_country(self, country: str) -> list:
        """Get news from API by country
        Args:
            country (str): country of news
        Returns:
            list: list of news
        """
        self.args["country"] = country
        return self.get_news()

    def get_news_by_page(self, page: int) -> list:
        """Get news from API by page
        Args:
            page (int): page of news
        Returns:
            list: list of news
        """
        self.args["page"] = page
        return self.get_news()

    def get_news_by_language(self, language: str) -> list:
        """Get news from API by language
        Args:
            language (str): language of news
        Returns:
            list: list of news
        """
        self.args["language"] = language
        return self.get_news()

    def get_news_by_page_size(self, page_size: int) -> list:
        """Get news from API by page size
        Args:
            page_size (int): page size of news
        Returns:
            list: list of news
        """
        self.args["pageSize"] = page_size
        return self.get_news()
