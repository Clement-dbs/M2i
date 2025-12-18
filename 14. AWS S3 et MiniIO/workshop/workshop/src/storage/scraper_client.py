import os

from bs4 import BeautifulSoup
from config.settings import scraper_config

class ScraperStorage:
    def __init__(self):
        self.client = BeautifulSoup(
            base_url = scraper_config.base_url,
            delay = scraper_config.delay,
            timeout= scraper_config.timeout,
            max_retries= scraper_config.max_retries,
            max_pages= scraper_config.max_pages
        )