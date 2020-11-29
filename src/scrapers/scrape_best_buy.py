import os

from src.dao.selenium_driver import SeleniumDriver

BEST_BUY_PS5_CONSOLE = os.environ. \
    get("BEST_BUY_PS5_CONSOLE",
        "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p")

BEST_BUY_PS5_DIGITAL = os.environ. \
    get("BEST_BUY_PS5_DIGITAL",
        "https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p")


class ScrapeBestBuy:
    def __init__(self, selenium_driver: SeleniumDriver):
        self.selenium_driver = selenium_driver

    def is_ps5_console_available(self):
        return self._is_available(BEST_BUY_PS5_CONSOLE)

    def is_ps5_digital_available(self):
        return self._is_available(BEST_BUY_PS5_DIGITAL)

    def _is_available(self, url: str):
        self.selenium_driver.get(url)
        self.selenium_driver.wait_by_class_name("sku-title")

        page_source = self.selenium_driver.page_source()

        if "Sony - PlayStation 5" not in page_source:
            return False

        status_text = self.selenium_driver.get_text_by_class_name('fulfillment-add-to-cart-button')

        if not status_text:
            return False
        elif "Sold Out" == status_text:
            return False
        else:
            return True
