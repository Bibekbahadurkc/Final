from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
            messages.info(request, 'You are successfully logged in')
        else:
            messages.info(request,'invalid password or username')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        em = request.POST['em']
        un = request.POST['un']
        pw = request.POST['pw']

        if User.objects.filter(username=un).exists():
            messages.info(request,'Username taken')
            return  redirect('register')
        else:
            user = User.objects.create_user(first_name=fn,last_name=ln, email=em, username=un, password=pw)
            user.save()
            messages.info(request,'User Created')
            return redirect('login')
    else:
        return render(request, 'register.html')



def do_logout(request):
    auth.logout(request)
    return redirect('/')
