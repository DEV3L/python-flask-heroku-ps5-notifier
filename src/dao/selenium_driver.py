import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = os.environ.get("CHROMEDRIVER_PATH",
                                   "/Users/dev3l/workspace/python-flask-heroku-ps5-notifier/drivers/chromedriver")
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN",
                                   '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
IS_HEADLESS = os.environ.get("HEADLESS", "True")
USER_AGENT = os.environ.get("USER_AGENT",
                            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/86.0.4240.198 Safari/537.36")


class SeleniumDriver:
    def __init__(self):
        options = Options()
        is_headless = IS_HEADLESS == "True"

        options.headless = is_headless
        options.binary_location = GOOGLE_CHROME_BIN
        options.add_argument("--start-maximized")
        options.add_argument("--kiosk")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument(f'--user-agent={USER_AGENT}')

        self.options = options
        self.driver = webdriver.Chrome(options=options, executable_path=CHROMEDRIVER_PATH)

    def quit(self):
        self.driver.quit()
