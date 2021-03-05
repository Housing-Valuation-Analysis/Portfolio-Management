"""Setup file"""
from setuptools import setup, find_packages

PACKAGES = find_packages()

LONG_DESCRIPTION = """
Portfolio Mangement
========
This is a portfolio management tool aimed at vaule investors
who are trying to compare multiple stock at the same time
and understand what is the best purchase. This project is
broken into two main parts:
1. Web interface
2. Python Scraper
========
"""

NAME = 'Portfolio Management'
VERSION = 0.1
URL = 'https://github.com/Housing-Valuation-Analysis/Portfolio-Management'
DESCRIPTION = 'Portfolio management tool'

opts = dict(name=NAME,
            version=VERSION,
            url=URL,
            packages=PACKAGES,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION)

if __name__ == '__main__':
    setup(**opts)
