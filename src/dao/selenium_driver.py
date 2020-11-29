import os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.services.logging_service import LoggingService

logger = LoggingService('SeleniumDriver')

CHROMEDRIVER_PATH = os.environ.get("CHROMEDRIVER_PATH",
                                   "/Users/dev3l/workspace/python-flask-heroku-ps5-notifier/drivers/chromedriver")
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN",
                                   '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
IS_HEADLESS = os.environ.get("HEADLESS", "True")
USER_AGENT = os.environ.get("USER_AGENT",
                            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/86.0.4240.198 Safari/537.36")

WAIT_TIME = 3

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

    def get(self, url: str):
        self.driver.get(url)

    def page_source(self) -> str:
        return self.driver.page_source

    def wait_by_class_name(self, class_name: str) -> bool:
        try:
            WebDriverWait(self.driver, WAIT_TIME).until(expected_conditions
                                                        .presence_of_element_located((By.CLASS_NAME, class_name)))
            return True
        except TimeoutException:
            logger.warning(f'Element with class {class_name} not found')
            return False

    def get_text_by_class_name(self, class_name: str) -> str:
        try:
            return self.driver.find_element_by_class_name(class_name).text
        except NoSuchElementException as e:
            logger.warning(f'Element with class {class_name} not found')
            return ""

    def quit(self):
        self.driver.quit()
