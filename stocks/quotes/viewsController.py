# pylint: disable=invalid-name, missing-module-docstring, wrong-import-position
# pylint: disable=missing-function-docstring, import-error


def retrieve_by_scraper(scraper):
    """Separated files for business logic."""

    data = scraper.scrape_all_data()
    return data.get('financials')
