from dotenv import load_dotenv

load_dotenv()

from src.scrapers.scraper_amazon import ScraperAmazon
from src.scrapers.scraper_best_buy import ScraperBestBuy
from src.scrapers.scraper_game_stop import ScraperGameStop
from src.scrapers.scraper_target import ScraperTarget
from src.services.twilio_service import TwilioService
from src.services.logging_service import LoggingService
from src.dao.selenium_driver import SeleniumDriver

logger = LoggingService('scrape_sites')


def check_site(scraper, twilio_service):
    if scraper.is_ps5_console_available():
        logger.info(f'PS5 Console AVAILABLE at {scraper.site_name}')
        twilio_service.send_message(f'PS5 Console Available at {scraper.site_name} - {scraper.ps5_console_url}')
    else:
        logger.info(f'PS5 Console not available at {scraper.site_name}')

    if scraper.is_ps5_digital_available():
        logger.info(f'PS5 Digital AVAILABLE at {scraper.site_name}')
        twilio_service.send_message(f'PS5 Console Available at {scraper.site_name} - {scraper.ps5_digital_url}')
    else:
        logger.info(f'PS5 Digital not available at {scraper.site_name}')


def run(selenium_driver, twilio_service):
    scraper_best_buy = ScraperBestBuy(selenium_driver)
    check_site(scraper_best_buy, twilio_service)

    scraper_amazon = ScraperAmazon(selenium_driver)
    check_site(scraper_amazon, twilio_service)

    scraper_game_stop = ScraperGameStop(selenium_driver)
    check_site(scraper_game_stop, twilio_service)

    scraper_target = ScraperTarget(selenium_driver)
    check_site(scraper_target, twilio_service)

    selenium_driver.quit()


if __name__ == "__main__":
    selenium_driver = SeleniumDriver()

    try:
        twilio_service = TwilioService()
        selenium_driver = SeleniumDriver()

        run(selenium_driver, twilio_service)
    except Exception as e:
        logger.exception(e)
    finally:
        selenium_driver.quit()
