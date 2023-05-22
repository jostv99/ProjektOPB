from django.shortcuts import render, redirect
from .forms import Sign_upForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def sign_up(response):
    if response.method == "POST":
        form = Sign_upForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, 'account created successfully')
        return redirect("/")
    else:
        form = Sign_upForm()
        
    return render(response, "sign_up/sign_up.html", {"form":form})


def login(response):
    if response.method == "POST":
        username = response.POST["username"]
        password = response.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            return login(response, user)
        else:
            return redirect("login/")