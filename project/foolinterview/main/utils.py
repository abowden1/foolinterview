import random
import json

import foolinterview.settings as config


class Articles:
    def __init__(self):
        self.file = config.CONTENT_FILE
        self.primary = {}
        self.secondary = []
        self.articles = self._load_articles()
        self.available_articles = self.articles

    def _load_articles(self):
        with open(self.file) as f:
            data = f.read()
        content = json.loads(data)['results']
        return content

    def generate_content(self):
        try:
            self._get_primary()
            self._get_secondary()
            return True
        except:
            return False

    def _get_primary(self):
        """
        finds the first article in the list of available with the slug
        defined in config. set that as the primary article
        :return: True on success, False when no article is found
        """
        for index, article in enumerate(self.available_articles):
            for tag in article['tags']:
                if tag['slug'] == config.FEATURED_ARTICLE_SLUG:
                    self.primary = self.available_articles.pop(index)
                    return True
        return False

    def _get_secondary(self):
        """
        of the remaining articles, stores additional articles to self.secondary, based
        on length defined in config.SECONDARY_ARTICLE_COUNT
        :return: True on success, False when no article is found
        """
        if not self.primary:
            self._get_primary()
        for i in range(config.SECONDARY_ARTICLE_COUNT):
            try:
                index = random.randint(0, len(self.available_articles)-1)
                self.secondary.append(self.available_articles.pop(index))
            except:
                pass
        # re-add to available articles for use later
        for article in self.secondary:
            self.available_articles.append(article)

    def get_article_by_uuid(self, uuid):
        for article in self.articles:
            if article['uuid'] == uuid:
                return article
        return False


class Quotes:
    def __init__(self):
        self.file = config.QUOTES_FILE
        self.quotes = self._load_quotes()

    def _load_quotes(self):
        with open(self.file) as f:
            data = f.read()
        quotes = json.loads(data)
        return quotes

