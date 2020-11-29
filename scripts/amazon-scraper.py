from dotenv import load_dotenv

from src.services.scraper_amazon_service import ScraperAmazonService

load_dotenv()

if __name__ == '__main__':
    walmart_scraper_service = ScraperAmazonService()
    walmart_scraper_service.is_console_available()
