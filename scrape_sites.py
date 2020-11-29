from dotenv import load_dotenv

from src.services.twilio_service import TwilioService

load_dotenv()

from src.services.logging_service import LoggingService
from src.dao.selenium_driver import SeleniumDriver
from src.scrapers.scrape_best_buy import ScrapeBestBuy, BEST_BUY_PS5_CONSOLE, BEST_BUY_PS5_DIGITAL

logger = LoggingService('scrape_sites')

if __name__ == "__main__":
    twilio_service = TwilioService()
    selenium_driver = SeleniumDriver()

    scrape_best_buy = ScrapeBestBuy(selenium_driver)

    if scrape_best_buy.is_ps5_console_available():
        logger.info("PS5 Console AVAILABLE at Best Buy")
        twilio_service.send_message(f'PS5 Console Available at Best Buy - {BEST_BUY_PS5_CONSOLE}')
    else:
        logger.info("PS5 Console not available at Best Buy")

    if scrape_best_buy.is_ps5_digital_available():
        logger.info("PS5 Digital AVAILABLE at Best Buy")
        twilio_service.send_message(f'PS5 Console Available at Best Buy - {BEST_BUY_PS5_DIGITAL}')
    else:
        logger.info("PS5 Digital not available at Best Buy")

    selenium_driver.quit()
