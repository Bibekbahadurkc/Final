from django.shortcuts import render

# Create your views here.
def serv(request):
    return render(request, "services.html")