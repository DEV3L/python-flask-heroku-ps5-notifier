import os

import requests
from bs4 import BeautifulSoup

from src.services.logging_service import LoggingService

logger = LoggingService('ScraperAmazonService')


class ScraperAmazonService:
    URL = os.environ.get('AMAZON_PS5_CONSOLE', 'https://www.walmart.com/')

    def __init__(self, *, url: str = URL):
        self.url = 'https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG/'

    def is_console_available(self) -> bool:
        soup = self._get_soup_from_url()

        available_div = soup.findAll("div", {"class": "prod-blitz-copy-message"})

        logger.info('Done writing files')

    def _get_soup_from_url(self) -> BeautifulSoup:
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "httpbin.org",
            "Referer": "https://www.codementor.io/@scrapingdog/10-tips-to-avoid-getting-blocked-while-scraping-websites-16papipe62",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
            "X-Amzn-Trace-Id": "Root=1-5fc2d8f5-6d2bea19234d7b3d2ea3e357"
        }

        url_object = requests.get(self.url, header)

        logger.info(f'Read {self.url}')
        full_html = url_object.read()

        return BeautifulSoup(full_html, 'html.parser')
