class tickerError(Exception):
    def __init__(self, stock):
        mess = str(stock) + ' Is an Invalid Ticker, please try again'
        self.message = mess
        super().__init__(self.message)
        
class urlError(Exception):
    def __init__(self, url):
        mess = str(url) + ' Is an Invalid URL, please try again'
        self.message = mess
        super().__init__(self.message)
        
class dataError(Exception):
    def __init__(self, stock):
        mess = str(stock) + ' has no data, please try again'
        self.message = mess
        super().__init__(self.message)
        
class inputError(Exception):
    def __init__(self):
        mess = 'The input data is not in proper format.\n\t\tPossible code tampering'
        self.message = mess
        super().__init__(self.message)