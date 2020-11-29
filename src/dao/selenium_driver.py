import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN",
                                   '/Users/dev3l/workspace/python-flask-heroku-ps5-notifier/drivers/chromedriver')
IS_HEADLESS = os.environ.get("HEADLESS", "True")
USER_AGENT = os.environ.get("USER_AGENT",
                            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/86.0.4240.198 Safari/537.36")


class SeleniumDriver:
    def __init__(self):
        options = Options()
        is_headless = IS_HEADLESS == "True"

        options.headless = is_headless
        options.add_argument("--start-maximized")
        options.add_argument("--kiosk")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        self.options = options
        self.driver = webdriver.Chrome(options=options, executable_path=GOOGLE_CHROME_BIN)

    def quit(self):
        self.driver.quit()
