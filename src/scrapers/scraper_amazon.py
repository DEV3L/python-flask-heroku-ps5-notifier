import os

from src.dao.selenium_driver import SeleniumDriver
from src.scrapers.scraper import Scraper

AMAZON_PS5_CONSOLE = os.environ. \
    get("AMAZON_PS5_CONSOLE",
        "https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG")

AMAZON_PS5_DIGITAL = os.environ. \
    get("AMAZON_PS5_DIGITAL",
        "https://www.amazon.com/PlayStation-5-Digital/dp/B08FC6MR62")


class ScraperAmazon(Scraper):
    def __init__(self, selenium_driver: SeleniumDriver):
        Scraper.__init__(self, selenium_driver, "Amazon", AMAZON_PS5_CONSOLE, AMAZON_PS5_DIGITAL)

    def _is_available(self, url: str):
        self.selenium_driver.get(url)
        self.selenium_driver.wait_by_id("productTitle")

        page_source = self.selenium_driver.page_source()

        if "playstation 5" not in page_source.lower():
            return False

        status_text = self.selenium_driver.get_text_by_id('availability')

        if not status_text:
            return False
        elif "currently unavailable" in status_text.lower():
            return False
        else:
            return True
