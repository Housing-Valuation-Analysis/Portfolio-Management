"""This modules contains the errors for the website"""


class InvalidFormError(Exception):
    """Error for invalid form"""
    def __init__(self):
        self.message = "Invalid form"
        super().__init__(self.message)
