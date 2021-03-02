# pylint: disable=no-member
# pylint: disable=broad-except

"""Website views"""
import json
import requests
from django.shortcuts import render, redirect
from django.contrib import messages
# from stocks.errors import InvalidFormError
from .models import Stock
from .forms import StockForm
import sys

# sys.path.insert(1, '/Users/vincentlan/Documents/GitHub/Portfolio-Management-branch2/')
from scraping.scraper import Scraper
from django import template

register = template.Library()


# Create your views here.
def home_view(request):
    """The home view"""

    if request.method == "POST":
        ticker = request.POST['ticker']
        scraper = Scraper(ticker)
        data = scraper.scrape_all_data()
        # api_request = requests.get(
        #     "https://cloud.iexapis.com/stable/stock/"
        #     + ticker
        #     + "/quote?token=pk_73eb0d679f5f4f73b7d17b90e50923af"
        # )

        try:
            financials_data = data.get('financials')
        except Exception:
            financials_data = "Error..."
        return render(request, 'home.html', {'financials_data': financials_data})
    return render(
        request,
        'home.html',
        {
            'ticker': "Enter a ticker symbol above"
        }
    )


def about_view(request):
    """The about view"""
    return render(request, 'about.html', {})


def dashboard_view(request):
    """The dashboard view"""
    if request.method == "POST":
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Stock has been added!")
            return redirect('dashboard')
        # raise InvalidFormError()
    ticker = Stock.objects.all()
    output = []

    for ticker_item in ticker:
        scraper = Scraper(str(ticker_item))
        try:
            data = scraper.scrape_all_data()
            financials_data = data.get('financials')
            output.append(financials_data)
        except Exception:
            api = "Error..."
    # mylist = zip(output, ticker)
    # context = {
    #     'mylist': mylist,
    # }
    return render(
        request,
        'dashboard.html',
        {'ticker': ticker,
         'output': output
         }
    )


def delete(request, stock_id):
    """The delete view"""
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, "Stock has been delete!")
    return redirect(dashboard_view)
