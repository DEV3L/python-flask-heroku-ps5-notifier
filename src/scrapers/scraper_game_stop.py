import os

from src.dao.selenium_driver import SeleniumDriver
from src.scrapers.scraper import Scraper

GAME_STOP_PS5_CONSOLE = os.environ. \
    get("GAME_STOP_PS5_CONSOLE",
        "https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html")

GAME_STOP_PS5_DIGITAL = os.environ. \
    get("GAME_STOP_PS5_DIGITAL",
        "https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5-digital-edition/11108141.html")


class ScraperGameStop(Scraper):
    def __init__(self, selenium_driver: SeleniumDriver):
        Scraper.__init__(self, selenium_driver, "Game Stop", GAME_STOP_PS5_CONSOLE, GAME_STOP_PS5_DIGITAL)

    def _is_available(self, url: str):
        self.selenium_driver.get(url)
        self.selenium_driver.wait_by_class_name("product-name")

        page_source = self.selenium_driver.page_source()

        if "playstation 5" not in page_source.lower():
            return False

        status_text = self.selenium_driver.get_text_by_class_name('add-to-cart')

        if not status_text:
            return False
        elif "not available" in status_text.lower():
            return False
        else:
            return True
