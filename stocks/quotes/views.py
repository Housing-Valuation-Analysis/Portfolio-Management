# pylint: disable=no-member
# pylint: disable=broad-except
# pylint: disable=wrong-import-position
# pylint: disable=raise-missing-from

"""Website views"""
import sys
import os
from django.shortcuts import render, redirect
from django.contrib import messages
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(
        "Portfolio-Management-branch"), '..')))
from scraping.scraper import Scraper  # noqa: E402
from .models import Stock  # noqa: E402
from .forms import StockForm  # noqa: E402
from .viewsController import retrieve_by_ticker

# Create your views here.
def home_view(request):
    """The home view"""

    if request.method == "POST":
        ticker = request.POST['ticker']
        financials_data = retrieve_by_ticker(ticker)
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
        check_ticker = request.POST.get('ticker')
        scraper = Scraper(str(check_ticker))
        try:
            data = scraper.scrape_all_data()
        except KeyError:
            raise Exception

        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request,
                             "Stock has been added!"
                             )
            return redirect('dashboard')
    ticker = Stock.objects.all()
    output = []

    for ticker_item in ticker:
        output.append(retrieve_by_ticker(str(ticker_item)))

    zip_list = zip(output, ticker)
    return render(
        request,
        'dashboard.html',
        {'ticker': ticker,
         'output': output,
         'zip_list': zip_list
         }
    )


def delete(request, stock_id):
    """The delete view"""
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, "Stock has been delete!")
    return redirect(dashboard_view)
