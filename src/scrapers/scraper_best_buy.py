import os

from src.dao.selenium_driver import SeleniumDriver
from src.scrapers.scraper import Scraper

BEST_BUY_PS5_CONSOLE = os.environ. \
    get("BEST_BUY_PS5_CONSOLE",
        "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p")

BEST_BUY_PS5_DIGITAL = os.environ. \
    get("BEST_BUY_PS5_DIGITAL",
        "https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p")


class ScraperBestBuy(Scraper):
    def __init__(self, selenium_driver: SeleniumDriver):
        Scraper.__init__(self, selenium_driver, "Best Buy", BEST_BUY_PS5_CONSOLE, BEST_BUY_PS5_DIGITAL)

    def _is_available(self, url: str):
        self.selenium_driver.get(url)
        self.selenium_driver.wait_by_class_name("sku-title")

        page_source = self.selenium_driver.page_source()

        if "sony - playstation 5" not in page_source.lower():
            return False

        status_text = self.selenium_driver.get_text_by_class_name('fulfillment-add-to-cart-button')

        if not status_text:
            return False
        elif "sold out" in status_text.lower():
            return False
        else:
            return True
