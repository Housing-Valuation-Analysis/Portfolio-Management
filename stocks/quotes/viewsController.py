# pylint: disable=invalid-name, missing-module-docstring, wrong-import-position
# pylint: disable=missing-function-docstring, import-error

from scraping.scraper import Scraper  # noqa:E402


def retrieve_by_ticker(ticker):
    return retrieve_by_scraper(Scraper(ticker))


# Separated into two functions for testing purpose
def retrieve_by_scraper(scraper):

    data = scraper.scrape_all_data()
    return data.get('financials')
