from django.urls import path

from Booking import views

urlpatterns = [
    path('add/<int:pk>', views.show_price),
    path('', views.show_book),
    path("delete/<int:pk>", views.delete),

]