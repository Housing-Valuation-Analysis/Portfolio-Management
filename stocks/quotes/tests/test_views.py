"""Module containing the tests for the website integration with scraper"""

import os
import sys
import unittest

from django.test import TestCase
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname("Portfolio-Management-branch"), '..')))
from scraping import Scraper
from scraping.clients import Requester
from ..viewsController import retrieve_by_scraper

TEST_TICKER = 'MSFT'
VALID_PROFILE_URL_TEXT_FILE_NAME = 'valid_profile_url_text.html'
VALID_KEY_STATISTICS_URL_TEXT_FILE_NAME = 'valid_key_statistics_url_text.html'

class TestScraper(TestCase):
    """Class with the tests for the scraper integration"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_dir = os.path.join("quotes", "tests", "data")
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

    def empty_function(self):
        pass

    def test_retrieve_from_scraper(self):
        test_data = os.path.join(
            self.data_dir,
            VALID_KEY_STATISTICS_URL_TEXT_FILE_NAME)
        test_requester = TestScraper.get_test_requester(test_data)
        test_scraper = TestScraper.get_test_scraper(test_requester)
        test_scraper.add_profile_to_dict = self.empty_function
        self.assertTrue(retrieve_by_scraper(test_scraper)['Gross Profits'] == '96.94B')

        test_data = os.path.join(
            self.data_dir,
            VALID_PROFILE_URL_TEXT_FILE_NAME)
        test_requester = TestScraper.get_test_requester(test_data)
        test_scraper = TestScraper.get_test_scraper(test_requester)
        test_scraper.add_key_stats_to_dict = self.empty_function
        self.assertTrue(retrieve_by_scraper(test_scraper)['Sector'] == 'Technology')