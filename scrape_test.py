from src.dao.selenium_driver import SeleniumDriver

selenium_driver = SeleniumDriver()

driver = selenium_driver.driver

driver.get("https://www.google.com")

print(driver.page_source)

selenium_driver.quit()
