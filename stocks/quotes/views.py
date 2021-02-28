from django.shortcuts import render, redirect
from .models import Stock
from django.core.exceptions import ObjectDoesNotExist
from .forms import StockForm
from django.contrib import messages
import sys
sys.path.insert(1, '/Users/vincentlan/Documents/GitHub/Portfolio-Management/')
from scraping.scraper import Scraper
from django import template
register = template.Library()

# Create your views here.
def home_view(request):
    import requests
    import json
    
    if request.method == "POST":
        ticker = request.POST['ticker']
        print(type(ticker))
        scraper = Scraper(ticker)
        data = scraper.scrape_all_data()
        # print(data)
        # api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_73eb0d679f5f4f73b7d17b90e50923af")
        # print(api_request.content)
        try:
            financials_data = data.get('financials')          
        except Exception as e:
            # api = "Error..."
            financials_data = "Error..."
        return render(request, 'home.html', {'financials_data': financials_data})
    else:
        return render(request, 'home.html', {'ticker': "Enter a ticker symbol above"})

    return render(request, 'home.html', {'financials_data' : financials_data})

def about_view(request):
    return render(request, 'about.html', {})

def dashboard_view(request):
    import requests
    import json
    if request.method == "POST":
        form = StockForm(request.POST or None)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, "Stock has been added!")
            return redirect('dashboard')
        else:
            return redirect('dashboard')
    else:
        ticker = Stock.objects.all()
        output = []
        # print(ticker)
        for ticker_item in ticker:
            # print(str(ticker_item))
            scraper = Scraper(str(ticker_item))
            # data = scraper.scrape_all_data()
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ str(ticker_item) + "/quote?token=pk_73eb0d679f5f4f73b7d17b90e50923af")
        
            try:
                # financials_data = data.get('financials')
                # output.append(financials_data)
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                financials_data = "Error..."
        # return render(request, 'home.html', {'api' : api })
        
        # mylist = zip(output, ticker)
        # return render(request, 'add_stock.html', {'mylist': mylist})    
        # return render(request, 'dashboard.html', {'ticker': ticker, 'output': output})
        return render(request, 'dashboard.html', {'ticker': ticker, 'output': output})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, "Stock has been delete!")
    return redirect(dashboard_view)
