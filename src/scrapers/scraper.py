from src.dao.selenium_driver import SeleniumDriver


class Scraper:
    def __init__(self, selenium_driver: SeleniumDriver, site_name: str, ps5_console_url: str, ps5_digital_url):
        self.site_name = site_name
        self.ps5_console_url = ps5_console_url
        self.ps5_digital_url = ps5_digital_url

        self.selenium_driver = selenium_driver

    def is_ps5_console_available(self):
        return self._is_available(self.ps5_console_url)

    def is_ps5_digital_available(self):
        return self._is_available(self.ps5_digital_url)

    def _is_available(self, url: str):
        raise NotImplemented
