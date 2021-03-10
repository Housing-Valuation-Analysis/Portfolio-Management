# pylint: disable=invalid-str-returned
"""Models for website"""
from django.db import models
from datetime import date


# Create your models here.
class Stock(models.Model):
    """Stock model"""
    ticker = models.CharField(max_length=10, unique=True)
    entry_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)
    entry_date = models.DateField(default=date.today, blank=True)
    shares = models.DecimalField(max_digits=10, decimal_places=3, default=0, null=0, blank=True)

    def __str__(self):
        return self.ticker

    def clean(self):
        self.ticker = self.ticker.upper()
