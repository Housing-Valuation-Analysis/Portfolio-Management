# pylint: disable=wrong-import-order, wrong-import-position, import-error
# pylint: disable=missing-function-docstring
# pylint: disable=no-member
# pylint: disable=relative-beyond-top-level
# pylint: disable=broad-except
# pylint: disable=too-many-locals

"""Website views"""
import sys
import os
import csv
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(
        "Portfolio-Management-branch"), '..')))
from scraping.scraper import Scraper  # noqa: E402
from .models import Stock  # noqa: E402
from .forms import StockForm  # noqa: E402
from .viewsController import retrieve_by_ticker  # noqa: E402


# Create your views here.
def home_view(request):
    """The home view"""

    if request.method == "POST":
        ticker = request.POST['ticker']
        try:
            financials_data = retrieve_by_ticker(ticker)
        except Exception as exc:
            messages.error(request, exc.message)
            return redirect('dashboard')
        return render(
            request,
            'home.html',
            {'financials_data': financials_data}
            )
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

        output.append(retrieve_by_ticker(str(item_list[0])))

    zip_list = zip(output, ticker, price, date, share, obj)

    return render(
        request,
        'dashboard.html',
        {'ticker': ticker,
         'output': output,
         'zip_list': zip_list
         }
    )


def delete(request, stock_id):
    """delete view"""
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, "Stock has been delete!")
    return redirect(dashboard_view)


@permission_required('admi.can_add_log_entry')
def download_csv(request):
    """Write dashboard data as csv"""
    obj = Stock.objects.all()
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

    i = 0
    for ticker_item in ticker:
        scraper = Scraper(str(ticker_item))
        try:
            data = scraper.scrape_all_data()
            financials_data = data.get('financials')
        except Exception:
            messages.error(request, "Unable to download...")
            return redirect('dashboard')

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


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(
        request,
        'registration/register.html',
        {'form': form}
        )
