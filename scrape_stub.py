from src.dao.selenium_driver import SeleniumDriver

if __name__ == "__main__":
    selenium_driver = SeleniumDriver()
    driver = selenium_driver.driver

    driver.get("https://www.google.com")

    assert "Google" in driver.page_source

    selenium_driver.quit()

    print("Selenium with Chrome configured correctly")
