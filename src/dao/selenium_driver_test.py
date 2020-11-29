from unittest.mock import patch

from src.dao.selenium_driver import SeleniumDriver, GOOGLE_CHROME_BIN


@patch('src.dao.selenium_driver.Options')
@patch('src.dao.selenium_driver.webdriver')
def test_selenium_driver_initializes(mock_webdriver, mock_options):
    selenium_driver = SeleniumDriver()

    options_instance = mock_options.return_value

    options_instance.add_argument.assert_any_call("--start-maximized")
    options_instance.add_argument.assert_any_call("--kiosk")
    options_instance.add_argument.assert_any_call("--disable-dev-shm-usage")
    options_instance.add_argument.assert_any_call("--no-sandbox")

    assert selenium_driver.options == options_instance

    mock_webdriver.Chrome.assert_called_with(options=options_instance, executable_path=GOOGLE_CHROME_BIN)

    assert selenium_driver.driver == mock_webdriver.Chrome.return_value
