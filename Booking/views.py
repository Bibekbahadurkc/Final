from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
from Booking.models import Book
from Pricing.models import Price


def show_price(request, pk):
    current_user = request.user
    booked = Price.objects.get(id=pk)
    Bo = Book(user=current_user, priced=booked, )
    Bo.save()
    messages.info(request, 'The booking is made.')
    return redirect('../')


def show_book(request):
    if request.method == 'POST':
        pri = request.POST['items']
        date = datetime.now()
        be = Book.objects.get(id=request.POST['ID'])
        be.priced = Price(id=pri)
        be.date = date
        be.save()
    current_user = request.user
    booked = Book.objects.all()
    prices = Price.objects.all()
    return render(request, 'booking.html', {'user_book': booked, 'current_user': current_user, 'pricing': prices})


def delete(request, pk):
    obj = Book.objects.get(id=pk)
    obj.delete()
    messages.info(request, 'Booking cancelled.')
    return redirect('../')