"""This modules contains the errors that we want to catch during scraping"""

class TickerError(Exception):
    """Error for nonexistent ticker"""
    def __init__(self, stock):
        mess = str(stock) + ' Is an Invalid Ticker, please try again'
        self.message = mess
        super().__init__(self.message)

class UrlError(Exception):
    """Error for an nonexistent input url"""
    def __init__(self, url):
        mess = str(url) + ' Is an Invalid URL, please try again'
        self.message = mess
        super().__init__(self.message)

class DataError(Exception):
    """Error for existent ticker, but no data at the url"""
    def __init__(self, stock):
        mess = str(stock) + ' is not a valid ticker, please try again'
        self.message = mess
        super().__init__(self.message)

class FileFormatError(Exception):
    """Error for data being in impropper format"""
    def __init__(self):
        mess = 'The input data is not in proper format.\n\t\tPossible code tampering'
        self.message = mess
        super().__init__(self.message)
