# pylint: disable=invalid-str-returned
"""Models for website"""
from django.db import models


# Create your models here.
class Stock(models.Model):
    """Stock model"""
    ticker = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.ticker

    def clean(self):
        self.ticker = self.ticker.upper()
