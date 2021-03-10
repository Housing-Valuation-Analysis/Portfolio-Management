"""Module containing scraper class used to scrape data
about provided ticker symbol"""

import re
import json
from bs4 import BeautifulSoup
from scraping.clients import Requester
from scraping.constants import URL_KEY_STATISTICS, URL_PROFILE
from scraping.errors import TickerError, UrlError, DataError, FileFormatError
from scraping.metrics_string_process import MetricStringProcessor


class Scraper:
    """Class used to scrape data
    about provided ticker symbol"""
    def __init__(self, ticker, requester=Requester()):
        self.ticker = ticker.upper()
        self.requester = requester
        self.string_processor = MetricStringProcessor()
        self.url_stats = URL_KEY_STATISTICS.format(self.ticker, self.ticker)
        self.url_profile = URL_PROFILE.format(self.ticker, self.ticker)
        self.financials_dict = {}
        self.sec_filing_list = []

    def parse_url(self, url):
        """Parses given yahoo endpoint for instance ticker"""
        try:
            text = self.requester.get_page_text(url)
        except Exception:
            raise UrlError(url) from None
        soup = BeautifulSoup(text, 'lxml')
        pattern = re.compile(r'\s--\sData\s--\s')
        script_data = soup.find('script', text=pattern).contents[0]
        start_pos = script_data.find("context") - 2
        end_pos = -12
        json_loads = json.loads(script_data[start_pos: end_pos])
        try:
            context = json_loads['context']
            dispatcher = context['dispatcher']
            stores = dispatcher['stores']
            quotes_summary_store = stores['QuoteSummaryStore']
        except KeyError:
            raise TickerError(self.ticker) from None
        return quotes_summary_store

    def add_to_data_dict(self, dic):
        """Safely unpacks dictionary and saves to local dict"""
        for item_key, item_val in dic.items():
            try:
                processed = self.string_processor.process_metrics(item_key)
                self.financials_dict[processed] = item_val['fmt']
            except (KeyError, TypeError):
                continue

    def add_key_stats_to_dict(self):
        """Adds keystats to local dict"""
        stats_data = self.parse_url(self.url_stats)
        tables_to_scrape = [
            'financialData',
            'summaryDetail',
            'defaultKeyStatistics',
            'price',
            'calendarEvents'
        ]
        if 'financialData' not in stats_data:
            raise DataError(self.ticker) from None
        for table in tables_to_scrape:
            self.add_to_data_dict(stats_data[table])

    def add_profile_to_dict(self):
        """Adds profile data to local dict"""
        profile_data = self.parse_url(self.url_profile)
        self.scrape_company_description(profile_data)
        self.scrape_company_name(profile_data)
        self.scrape_sec_filling(profile_data)

    def scrape_company_description(self, profile_data):
        """Scrapes company description"""
        asset_profile = profile_data['assetProfile']
        profile_fields_to_include = [
            'sector',
            'industry',
            "longBusinessSummary"
        ]
        for field in profile_fields_to_include:
            processed = self.string_processor.process_metrics(field)
            self.financials_dict[processed] = asset_profile.get(field)

    def scrape_company_name(self, profile_data):
        """Scrapes company name"""
        self.financials_dict['Company'] = profile_data['price']['shortName']

    def scrape_sec_filling(self, profile_data):
        """Scrapes sec filing data"""
        try:
            sec_filings = profile_data['secFilings']['filings']
            self.financials_dict["Latest SEC Filing"] =\
                sec_filings[0].get('edgarUrl')
            num = min(3, len(sec_filings))
            sec_fields_to_include = [
                'date',
                'type',
                'title',
                'edgarUrl'
            ]
            if sec_filings:
                for i in range(num):
                    temp_filing_dict = {}
                    for field in sec_fields_to_include:
                        temp_filing_dict[field] = sec_filings[i].get(field)
                    self.sec_filing_list.append(temp_filing_dict)
            # SEC Filling successful
            return True
        except KeyError:
            # No SEC Filling Info on Yahoo Finance
            raise FileFormatError from None

    def scrape_all_data(self):
        """Scrapes all data"""
        self.add_key_stats_to_dict()
        self.add_profile_to_dict()
        return {
            'financials': self.financials_dict,
            'sec_filings': self.sec_filing_list
        }

'''
if __name__ == "__main__":
    s = Scraper('MSFT')
    data = s.scrape_all_data()
    # print(data.keys())
    # print(data)
    # print(data["financials"])
    for key, val in data["financials"].items():
        print(key + ":" + val)
    # print(data['sec_filings'])
'''