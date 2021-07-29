from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import requests
from pycoingecko import CoinGeckoAPI

# Create your views here.
def home(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()
    return render(request, 'base.html', {'data': data[0:5]})


def price(request):
    cg = CoinGeckoAPI()
    if request.method == 'GET':
        price1 = cg.get_price(ids=['bitcoin', 'ethereum', 'tether','cardano', 'binancecoin'], vs_currencies='usd')
        price2 = price1.values()

        bitcoin = price1.get('bitcoin').get('usd')
        ethereum = price1.get('ethereum').get('usd')
        tether = price1.get('tether').get('usd')
        cardano = price1.get('cardano').get('usd')
        binancecoin = price1.get('binancecoin').get('usd')

        return JsonResponse({'bitcoin':bitcoin, 'ethereum':ethereum, 'tether':tether, 'cardano':cardano, 'bnb':binancecoin})
