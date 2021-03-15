# pylint: disable=no-member
# pylint: disable=broad-except

# pylint: disable=wrong-import-position
# pylint: disable=raise-missing-from

"""Website views"""
import sys
import os
import csv
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(
        "Portfolio-Management-branch"), '..')))
from scraping.scraper import Scraper  # noqa: E402
from .models import Stock  # noqa: E402
from .forms import StockForm # noqa: E402
from .viewsController import retrieve_by_scraper


# Create your views here.
def home_view(request):
    """The home view"""

    if request.method == "POST":
        ticker = request.POST['ticker']
        try:
            financials_data = retrieve_by_scraper(Scraper(ticker))
        except Exception as exc:
            messages.error(request, exc.message)
            return redirect('dashboard')


        return render(request, 'home.html', {'financials_data': financials_data})
    return render(
        request,
        'home.html',
        {
            'ticker': "Enter a ticker symbol above"
        }
    )

# def home_view(request):
#     """The home view"""
#
#     if request.method == "POST":
#         ticker = request.POST['ticker']
#         scraper = Scraper(ticker)
#         data = scraper.scrape_all_data()
#
#         try:
#             financials_data = data.get('financials')
#         except Exception:
#             financials_data = "Error..."
#         return render(request, 'home.html', {'financials_data': financials_data})
#     return render(
#         request,
#         'home.html',
#         {
#             'ticker': "Enter a ticker symbol above"
#         }
#     )


def about_view(request):
    """The about view"""
    return render(request, 'about.html', {})


def dashboard_view(request):
    """The dashboard view"""
    if request.method == "POST":

        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request,
                             "Stock has been added!"
                             )
            return redirect('dashboard')

    obj = Stock.objects.all()
    output = []
    ticker = []
    price = []
    share = []
    date = []

    for item in obj:
        item_list = str(item).split(',')
        ticker.append(item_list[0])
        price.append(item_list[1])
        date.append(item_list[2])
        share.append(item_list[3])

        output.append(retrieve_by_scraper(Scraper(str(item_list[0]))))

    zip_list = zip(output, ticker, price, date, share, obj)

    return render(
        request,
        'dashboard.html',
        {'ticker': ticker,
         'output': output,
         'zip_list': zip_list
         }
    )

#delete view
def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, "Stock has been delete!")
    return redirect(dashboard_view)


@permission_required('admi.can_add_log_entry')
def download_csv(request):
    """Write dashboard data as csv"""
    obj = Stock.objects.all()
    output = []
    ticker = []
    price = []
    share = []
    date = []

    for item in obj:
        item_list = str(item).split(',')
        ticker.append(item_list[0])
        price.append(item_list[1])
        date.append(item_list[2])
        share.append(item_list[3])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="stocks.csv'

    writer = csv.writer(response, delimiter=',')
    writer.writerow([
        'Sector',
        'Industry',
        'Stock Ticker',
        'Entry Price',
        'Entry Date',
        'Shares',
        'Current Price',
        'Beta',
        'PEG',
        'P/E (Trailing)',
        'P/E (Forward)',
        'P/B',
        'EV/EBITDA'
        ])

    i=0
    for ticker_item in ticker:
        scraper = Scraper(str(ticker_item))
        try:
            data = scraper.scrape_all_data()
            financials_data = data.get('financials')
        except Exception:
            api = "Error..."

        writer.writerow([
            financials_data['Sector'],
            financials_data['Industry'],
            str(ticker_item),
            price[i],
            date[i],
            share[i],
            financials_data['Current Price'],
            financials_data.get('Beta'),
            financials_data['PEG'],
            financials_data.get('P/E (Trailing)'),
            financials_data.get('P/E (Forward)'),
            financials_data.get('P/B'),
            financials_data.get('EV/EBITDA')
            ])
        i = i+1

    return response
