"""Module containing the tests for the website integration with scraper"""

import os
import unittest

from scraping import Scraper
from scraping.clients import Requester
#from stocks.quotes.views import home_view

TEST_TICKER = 'MSFT'
VALID_PROFILE_URL_TEXT_FILE_NAME = 'valid_profile_url_text.html'
VALID_KEY_STATISTICS_URL_TEXT_FILE_NAME = 'valid_key_statistics_url_text.html'

class TestScraper(unittest.TestCase):
    """Class with the tests for the scraper integration"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_dir = os.path.join("stocks", "quotes", "tests", "data")
        self.data_dir = self.data_dir if os.path.isdir(self.data_dir) \
            else os.path.join("data")

    @staticmethod
    def get_test_requester(file_to_read_text_from):
        """Gets the mock requester"""
        requester = Requester()

        def get_local_page_text(placeholder):
            with open(file_to_read_text_from, 'r') as file:
                text = file.read()
                return text

        requester.get_page_text = get_local_page_text
        return requester

    @staticmethod
    def get_test_scraper(requester=Requester()):
        """Gets the test scraper"""
        return Scraper(TEST_TICKER, requester)

    class test_request():
        def __init__(self):
            self.method = "POST"
            self.POST = {"ticker": TEST_TICKER}

    def fake_home_view(self, request):
        if request.method == "POST":
            ticker = request.POST['ticker']
            scraper = Scraper(ticker)
            data = scraper.scrape_all_data()

            try:
                financials_data = data.get('financials')
            except Exception:
                financials_data = "Error..."
            return financials_data

    def test_home_view_info_correctness(self):
        mock_request = self.test_request()
        self.assertTrue(self.fake_home_view(mock_request)['Gross Profits'] == '96.94B')
        self.assertTrue(self.fake_home_view(mock_request)['Sector'] == 'Technology')
