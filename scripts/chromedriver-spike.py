import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_by_class_name(web_driver, class_name):
    WebDriverWait(web_driver, 3).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, class_name)))


chrome_location = os.environ.get("GOOGLE_CHROME_BIN",
                                 '/Users/dev3l/workspace/python-flask-heroku-ps5-notifier/drivers/chromedriver')

options = Options()
# options.headless = True
options.add_argument("--start-maximized")
options.add_argument("--kiosk")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
# options.add_argument("--disable-blink-features")
# options.add_argument("--disable-blink-features=AutomationControlled")
#
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options, executable_path=chrome_location)

# driver.execute_cdp_cmd('Network.setUserAgentOverride', {
#     "userAgent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'})

# script = '''
# Object.defineProperty(navigator, 'webdriver', {
#     get: () => undefined
# })
# '''
# driver.execute_script(script)

# time.sleep(3)

# driver.get("https://www.walmart.com/ip/PlayStation-5-Console/363472942")


driver.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")

# driver.get("https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG")


if "Verify your identity" in driver.page_source:
    print("Blocked by captcha")
    exit(1)

print(driver.page_source)

driver.quit()
