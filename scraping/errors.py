class TickerError(Exception):
    def __init__(self, stock):
        mess = str(stock) + ' Is an Invalid Ticker, please try again'
        self.message = mess
        super().__init__(self.message)
        
class UrlError(Exception):
    def __init__(self, url):
        mess = str(url) + ' Is an Invalid URL, please try again'
        self.message = mess
        super().__init__(self.message)
        
class DataError(Exception):
    def __init__(self, stock):
        mess = str(stock) + ' is not a valid ticker, please try again'
        self.message = mess
        super().__init__(self.message)
        
class FileFormatError(Exception):
    def __init__(self):
        mess = 'The input data is not in proper format.\n\t\tPossible code tampering'
        self.message = mess
        super().__init__(self.message)