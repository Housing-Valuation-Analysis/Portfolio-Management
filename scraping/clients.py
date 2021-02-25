import requests

"""This module gives us the classes that we need associated with the requests library"""
class Requester:
    """This class has the function that we use to interface with the requests library"""
    def get_page_text(self, url):
        return requests.get(url).text
        