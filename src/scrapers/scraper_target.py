import os

from src.dao.selenium_driver import SeleniumDriver
from src.scrapers.scraper import Scraper

TARGET_PS5_CONSOLE = os.environ. \
    get("TARGET_PS5_CONSOLE",
        "https://www.target.com/p/playstation-5-console/-/A-81114595")

TARGET_PS5_DIGITAL = os.environ. \
    get("TARGET_PS5_DIGITAL",
        "https://www.target.com/p/playstation-5-digital-edition-console/-/A-81114596")


class ScraperTarget(Scraper):
    def __init__(self, selenium_driver: SeleniumDriver):
        Scraper.__init__(self, selenium_driver, "Target", TARGET_PS5_CONSOLE, TARGET_PS5_DIGITAL)

    def _is_available(self, url: str):
        self.selenium_driver.get(url)
        self.selenium_driver.wait_by_css_selector('[data-test="product-title"]')

        page_source = self.selenium_driver.page_source()

        if "playstation 5" not in page_source.lower():
            return False

        status_text = self.selenium_driver.get_text_by_css_selector('[data-test="storeFulfillmentAggregator"]')

        if not status_text:
            return False
        elif "out of stock" in status_text.lower():
            return False
        else:
            return True
