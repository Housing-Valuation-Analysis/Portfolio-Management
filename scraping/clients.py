import requests

"""Client interfaces"""


class Requester:
    """Gets the text from an endpoint"""

    @staticmethod
    def get_page_text(url):
        return requests.get(url).text
