from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Ad
from .forms import CreateNewListing, CreateNewUser

def index(response):
    ads = Ad.objects.all()
    return render(response, "main/index.html", {"ads":ads})

def login(response):
    return render(response, "main/login.html", {})

def new_ad(response):
    if response.method == "POST":
        form = CreateNewListing(response.POST)
        
        if form.is_valid():
            title, price = form.cleaned_data["title"], form.cleaned_data["price"]
            t = Ad(title=title, price=price, seller=None)
            t.save()
        
        return HttpResponseRedirect("/")
           
    else:
        form = CreateNewListing()
        
    return render(response, "main/new_ad.html", {"form":form})


def sign_up(response):
    if response.method == "POST":
        form = CreateNewUser(response.POST)
        
        if form.is_valid():
            email, name = form.cleaned_data["email"], form.cleaned_data["name"]
            t = User(name=name, email=email)
            t.save()
        
        return HttpResponseRedirect("/")
           
    else:
        form = CreateNewUser()
        
    return render(response, "main/sign_up.html", {"form":form})
