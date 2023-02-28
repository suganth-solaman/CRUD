from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import User

def register(request):
    if request.method == "POST":
        data = request.POST
        name = data['name']
        email = data['email']
        pass1 = data['pass1']
        pass2 = data['pass2']
        profile = data['profile']
        if User.objects.filter(email=email).exists():
            messages.error(request, "email already exist")
        else:
            if pass2 == pass1:
                User.objects.create_user(username=name,email=email,password=pass1, profile=profile )
                messages.success(request, "registed succussfully")
            else:
                messages.error(request, "password not matched")

    return render(request, "register.html")

def home(request):

    return render(request, "home.html")


def login_pro(request):
    if request.method == "POST":
        data = request.POST
        email = data['email']
        password = data['pass1']
        cred = User.objects.filter(email=email)
        if cred.exists():
            name = cred[0].username
        print(email,password)
        user = authenticate(request, username=name, password=password)
        print(user)
        if user is not None :
            login(request, user)
            messages.success(request, "loged in succussfully")
            return redirect('home')
        else:
            print("not", user)
        # else:
        #     messages.error(request, "email not extisttr")
        #     print("not")

    return render(request, "login.html")
# Create your views here.

def signout(request):

    logout(request)
    messages.success(request, "loged out succussfully")
    return redirect('home')

def edit(request,pk):
    if request.method == "POST":
        data = request.POST
        name = data['name']
        email = data['email']
        profile = data['profile']

        pro = User.objects.get(id=pk)
        pro.username = name
        pro.email = email
        pro.profile = profile
        pro.save()
        messages.success(request, "changed  succussfully")
        return redirect('home')

    return render(request, "register.html")

def delete(request,pk):
    pro = User.objects.get(id=pk)
    pro.delete()
    messages.success(request, "changed  succussfully")
    return redirect('home')
