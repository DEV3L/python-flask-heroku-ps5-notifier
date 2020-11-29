from unittest.mock import patch, MagicMock

from selenium.common.exceptions import TimeoutException, NoSuchElementException

from src.dao.selenium_driver import SeleniumDriver, CHROMEDRIVER_PATH, GOOGLE_CHROME_BIN, IS_HEADLESS, USER_AGENT, \
    WAIT_TIME


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


@patch('src.dao.selenium_driver.webdriver')
def test_get(mock_webdriver):
    expected_url = "https://wwww.google.com"

    selenium_driver = SeleniumDriver()
    selenium_driver.get(expected_url)

    mock_driver = mock_webdriver.Chrome.return_value

    mock_driver.get.assert_called_with(expected_url)


@patch('src.dao.selenium_driver.webdriver')
def test_page_source(mock_webdriver):
    selenium_driver = SeleniumDriver()
    page_source = selenium_driver.page_source()

    mock_driver = mock_webdriver.Chrome.return_value

    assert mock_driver.page_source == page_source


@patch('src.dao.selenium_driver.WebDriverWait')
@patch('src.dao.selenium_driver.webdriver')
def test_wait_by_class_name_true(mock_webdriver, mock_webdriverwait):
    expected_class_name = "class-name"

    selenium_driver = SeleniumDriver()
    is_wait = selenium_driver.wait_by_class_name(expected_class_name)

    mock_driver = mock_webdriver.Chrome.return_value

    assert mock_webdriverwait.called
    mock_webdriverwait.assert_called_with(mock_driver, WAIT_TIME)
    assert mock_webdriverwait.return_value.until.called

    assert is_wait


@patch('src.dao.selenium_driver.WebDriverWait')
@patch('src.dao.selenium_driver.webdriver')
def test_wait_by_class_name_false(mock_webdriver, mock_webdriverwait):
    expected_class_name = "class-name"

    mock_webdriverwait.side_effect = MagicMock(side_effect=TimeoutException('Test'))

    selenium_driver = SeleniumDriver()
    is_wait = selenium_driver.wait_by_class_name(expected_class_name)

    mock_driver = mock_webdriver.Chrome.return_value

    assert mock_webdriverwait.called
    mock_webdriverwait.assert_called_with(mock_driver, WAIT_TIME)

    assert not is_wait


@patch('src.dao.selenium_driver.webdriver')
def test_get_text_by_class_name(mock_webdriver):
    expected_class_name = "class-name"

    selenium_driver = SeleniumDriver()
    text = selenium_driver.get_text_by_class_name(expected_class_name)

    mock_driver = mock_webdriver.Chrome.return_value

    mock_driver.find_element_by_class_name.assert_called_with(expected_class_name)
    assert mock_driver.find_element_by_class_name.return_value.text == text


@patch('src.dao.selenium_driver.webdriver')
def test_get_text_by_class_name_not_found(mock_webdriver):
    expected_class_name = "class-name"
    mock_driver = mock_webdriver.Chrome.return_value

    mock_driver.find_element_by_class_name.side_effect = MagicMock(side_effect=NoSuchElementException('Test'))

    selenium_driver = SeleniumDriver()
    text = selenium_driver.get_text_by_class_name(expected_class_name)

    mock_driver.find_element_by_class_name.assert_called_with(expected_class_name)
    assert not text


@patch('src.dao.selenium_driver.webdriver')
def test_quit(mock_webdriver):
    selenium_driver = SeleniumDriver()
    selenium_driver.quit()

    mock_driver = mock_webdriver.Chrome.return_value

    assert mock_driver.quit.called
