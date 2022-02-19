from django.urls import path

from User import views

urlpatterns = [
    path('login', views.login, name="login"),
    path("register", views.register, name = "register"),
    path('logout', views.do_logout, name="logout"),

]