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

opts = dict(name = 'Portfolio Management',
            version = 0.1,
            url = 'https://github.com/Housing-Valuation-Analysis/Portfolio-Management',
            packages = PACKAGES,
            description = 'Portfolio management tool',
            long_description = LONG_DESCRIPTION)

if __name__ == '__main__':
    setup(**opts)
