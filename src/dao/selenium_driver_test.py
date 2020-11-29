from unittest.mock import patch

from src.dao.selenium_driver import SeleniumDriver, CHROMEDRIVER_PATH, GOOGLE_CHROME_BIN, IS_HEADLESS, USER_AGENT


@patch('src.dao.selenium_driver.Options')
@patch('src.dao.selenium_driver.webdriver')
def test_selenium_driver_initializes(mock_webdriver, mock_options):
    expected_is_headless = IS_HEADLESS == "True"
    expected_user_agent = f'--user-agent={USER_AGENT}'

    selenium_driver = SeleniumDriver()

    options_instance = mock_options.return_value

    options_instance.add_argument.assert_any_call("--start-maximized")
    options_instance.add_argument.assert_any_call("--kiosk")
    options_instance.add_argument.assert_any_call("--disable-dev-shm-usage")
    options_instance.add_argument.assert_any_call("--no-sandbox")
    options_instance.add_argument.assert_any_call("--no-sandbox")
    options_instance.add_argument.assert_any_call(expected_user_agent)

    assert options_instance.headless == expected_is_headless
    assert options_instance.binary_location == GOOGLE_CHROME_BIN
    assert selenium_driver.options == options_instance

    mock_webdriver.Chrome.assert_called_with(options=options_instance, executable_path=CHROMEDRIVER_PATH)

    assert selenium_driver.driver == mock_webdriver.Chrome.return_value
