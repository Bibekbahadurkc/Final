from django.urls import path

from Pricing import views

urlpatterns=[
    path('', views.show_price),
]