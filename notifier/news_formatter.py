""" format message """


class NewsFormatter:
    """News formatter class."""

    def format_news_to_telegram_message(self, news: list) -> list:
        """Format news to telegram message.

        Args:
            news (list): list of news
        Returns:
            list: list of messages to send
        """
        article_list = []
        for article in news:
            article_list.append(
                f"{self.format_content(article)}\n{self.format_url(article)}\n\n"
            )
        return article_list

    def format_content(self, article: dict) -> str:
        """Format content of news.

        Args:
            article (dict): article of news

        Returns:
            str: content of news
        """
        return (
            article["description"] if "description" in article else article["content"]
        )

    def format_url(self, article: dict) -> str:
        """Format url of news.

        Args:
            article (dict): article of news

        Returns:
            str: url of news
        """
        return article["url"] if "url" in article else ""
