from bs4 import BeautifulSoup
import requests
from config.settings import scraper_config

class Scraper:
    def __init__(self):
        self.base_url = scraper_config.base_url
        self.delay = scraper_config.delay
        self.timeout = scraper_config.timeout
        self.max_retries = scraper_config.max_retries
        self.max_pages = scraper_config.max_pages

    def scrape(self):
        for page in range(1, self.max_pages + 1):
            url = f"{self.base_url}/page/{page}"
            response = self._fetch_page(url)
            if response:
                self._parse_page(response.content)

    def _fetch_page(self, url):
        for attempt in range(self.max_retries):
            try:
                response = requests.get(url, timeout=self.timeout)
                response.raise_for_status()
                return response
            except requests.RequestException as e:
                print(f"Attempt {attempt + 1} failed: {e}")
        return None

    def _parse_page(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        items = soup.find_all(class_='item-class')  # Replace with actual class
        for item in items:
            title = item.find(class_='title-class').get_text()  # Replace with actual class