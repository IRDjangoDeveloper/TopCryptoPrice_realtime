from django.urls import path
from .views import home, price
urlpatterns = [
    path('', home, name='home_url'),
    path('getprice', price, name='getprice'),
]
