from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages


# Create your views here.
def home_view(request):
    import requests
    import json

    if request.method == "POST":
        ticker = request.POST['ticker']
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/"
            + ticker
            + "/quote?token=pk_73eb0d679f5f4f73b7d17b90e50923af"
        )

        try:
            api = json.loads(api_request.content)
        except Exception:
            api = "Error..."
        return render(request, 'home.html', {'api': api})
    else:
        return render(
            request,
            'home.html',
            {
                'ticker': "Enter a ticker symbol above"
            }
        )

    return render(request, 'home.html', {'api': api})


def about_view(request):
    return render(request, 'about.html', {})


def dashboard_view(request):
    import requests
    import json
    if request.method == "POST":
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Stock has been added!")
            return redirect('dashboard')
    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request =\
                requests.get("https://cloud.iexapis.com/stable/stock/"
                             + str(ticker_item)
                             + "/quote?token="
                             + "pk_73eb0d679f5f4f73b7d17b90e50923af"
                             )

            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception:
                api = "Error..."
        # return render(request, 'home.html', {'api' : api })
        # mylist = zip(output, ticker)
        # return render(request, 'add_stock.html', {'mylist': mylist})

        return render(
            request,
            'dashboard.html',
            {'ticker': ticker,
             'output': output}
        )


def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, "Stock has been delete!")
    return redirect(dashboard_view)
