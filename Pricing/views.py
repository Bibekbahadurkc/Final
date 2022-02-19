from django.shortcuts import render

# Create your views here.
from Pricing.models import Price


def show_price(request):
    prices = Price.objects.all()
    return render(request, "pricing.html", {'Prices' : prices})