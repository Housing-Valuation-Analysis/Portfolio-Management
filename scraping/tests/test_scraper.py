# pylint: disable=unused-argument
"""Module containing the tests for the scraper"""

import os
import unittest
from scraping.scraper import Scraper
from scraping.clients import Requester
from scraping.errors import UrlError, TickerError, FileFormatError, DataError


TEST_TICKER = 'MSFT'
VALID_PROFILE_URL_TEXT_FILE_NAME = 'valid_profile_url_text.html'
VALID_KEY_STATISTICS_URL_TEXT_FILE_NAME = 'valid_key_statistics_url_text.html'
TEST_URL = 'https://some.url'
INVALID_URL = 'invalid.html'
INVALID_PROFILE_URL_TEXT_FILE_NAME = 'invalid_profile_url_text.html'
INVALID_KEY_STATISTICS_URL_TEXT_FILE_NAME = \
    'invalid_key_statistics_url_text.html'
INVALID_FINANCIAL_DATA_TEXT_FILE_NAME = \
    'invalid_key_statistics_url_text_no_financial_data.html'
INVALID_SEC_FILING_TEXT_FILE_NAME = \
    'invalid_profile_url_text_no_sec_filings.html'


class TestScraper(unittest.TestCase):
    """Class with the tests for the scraper"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_dir = os.path.join("tests", "data")
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

    def test_scraper_succesfully_scrapes_valid_key_statistics_url(self):
        """Test that scraper works on keystats in happy path"""
        test_data = os.path.join(
            self.data_dir,
            VALID_KEY_STATISTICS_URL_TEXT_FILE_NAME)
        test_requester = TestScraper.get_test_requester(test_data)
        test_scraper = TestScraper.get_test_scraper(test_requester)
        test_scraper.add_key_stats_to_dict()
        self.assertTrue(
            test_scraper.financials_dict['Gross Profits'] == '96.94B')

    def test_scraper_succesfully_scrapes_valid_profile_url(self):
        """Test that scraper works on profile in happy path"""
        test_data = os.path.join(
            self.data_dir,
            VALID_PROFILE_URL_TEXT_FILE_NAME)
        test_requester = TestScraper.get_test_requester(test_data)
        test_scraper = TestScraper.get_test_scraper(test_requester)
        test_scraper.add_profile_to_dict()
        self.assertTrue(test_scraper.financials_dict['Sector'] == 'Technology')

    def test_scraper_raises_urlerror_when_get_page_text_throws(self):
        """Test that we raise url error when get page text throws"""
        test_data = os.path.join(self.data_dir, INVALID_URL)
        test_requester = TestScraper.get_test_requester(test_data)
        test_scraper = TestScraper.get_test_scraper(test_requester)
        with self.assertRaises(UrlError):
            test_scraper.add_key_stats_to_dict()

    def test_scraper_raises_ticker_error_for_invalid_key_statistics_text(self):
        """Test that we raise ticker error for invalid key stats scrape"""
        test_data = os.path.join(
            self.data_dir,
            INVALID_KEY_STATISTICS_URL_TEXT_FILE_NAME)
        test_requester = TestScraper.get_test_requester(test_data)
        test_scraper = TestScraper.get_test_scraper(test_requester)
        with self.assertRaises(TickerError):
            test_scraper.add_key_stats_to_dict()

    def test_scraper_raises_ticker_error_for_invalid_profile_url_text(self):
        """Test that we raise ticker error for invalid profile scrape"""
        test_data = os.path.join(
            self.data_dir,
            INVALID_PROFILE_URL_TEXT_FILE_NAME)
        test_requester = TestScraper.get_test_requester(test_data)
        test_scraper = TestScraper.get_test_scraper(test_requester)
        with self.assertRaises(TickerError):
            test_scraper.add_profile_to_dict()

    def test_scraper_raises_data_error_when_it_should(self):
        """Test that we raise data error when financial data does not exist"""
        test_data = os.path.join(
            self.data_dir,
            INVALID_FINANCIAL_DATA_TEXT_FILE_NAME)
        test_requester = TestScraper.get_test_requester(test_data)
        test_scraper = TestScraper.get_test_scraper(test_requester)
        with self.assertRaises(DataError):
            test_scraper.add_key_stats_to_dict()

    def test_scraper_raises_file_format_error_when_it_should(self):
        """Test that we raise file format error without financial data"""
        test_data = os.path.join(
            self.data_dir,
            INVALID_SEC_FILING_TEXT_FILE_NAME)
        test_requester = TestScraper.get_test_requester(test_data)
        test_scraper = TestScraper.get_test_scraper(test_requester)
        with self.assertRaises(FileFormatError):
            test_scraper.add_profile_to_dict()
