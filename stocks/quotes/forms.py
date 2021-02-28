# pylint: disable=too-few-public-methods
"""Module containing the forms"""
from django import forms
from .models import Stock


class StockForm(forms.ModelForm):
    """Class for the stock form"""
    class Meta:
        """Meta class for stock"""
        model = Stock
        fields = ["ticker"]
