"""Client interfaces"""
import requests


# Bad rules
# pylint: disable=R0903
class Requester:
    """Class that makes requests from an endpoint"""

    @staticmethod
    def get_page_text(url):
        """Perform get on the endpoint"""
        return requests.get(url).text
