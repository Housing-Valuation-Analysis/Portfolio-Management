from scraping.scraper import Scraper

def retrieve_by_ticker(ticker):
    return retrieve_by_scraper(Scraper(ticker))

def retrieve_by_scraper(scraper):
    try:
        data = scraper.scrape_all_data()
        financials_data = data.get('financials')
    except Exception:
        financials_data = "Error..."
    return financials_data