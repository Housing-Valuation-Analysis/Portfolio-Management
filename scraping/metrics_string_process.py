"""Contains class to convert json names to friendly ones"""

import stringcase


class MetricStringProcessor:
    """Class that converts json text to friendly text"""
    acronym = {"Peg Ratio": "PEG",
               "Trailing P E": "Trailing P/E",
               "Price To Sales Trailing12 Months": "P/Sales (TTM)",
               "Average Daily Volume3 Month": "Average Daily Volume (3M)",
               "Sand P52 Week Change": "S&P 52 Week Change",
               "Enterprise To EBITDA": "EV/EBITDA",
               "Enterprise To Revenue": "EV/Revenue",
               "Fifty Two Week Low": "52 Week Low",
               "Fifty Two Week High": "52 Week High",
               "Fifty Day Average": "50 Day Avg",
               "Two Hundred Day Average": "200 Day Avg",
               "Debt To Equity": "Debt/Equity"
               }

    def process_metrics(self, metric):
        """Process metric text"""
        metric = stringcase.titlecase(metric)
        metric = self.change_to_acronym(metric)
        words = metric.split()
        metric = " ".join([self.process_words(w) for w in words])
        return metric

    def process_words(self, word):
        """Process words"""
        word = self.process_ebitda(word)
        word = self.process_eps(word)
        return word

    @staticmethod
    def process_ebitda(word):
        """Process ebitda"""
        return word.upper() if word == "Ebitda" else word

    @staticmethod
    def process_eps(word):
        """Process eps"""
        return word.upper() if word == "Eps" else word

    def change_to_acronym(self, metric):
        """Converts metric to acronym value"""
        if metric in self.acronym:
            return self.acronym[metric]
        return metric
