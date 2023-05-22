from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Ad
from .forms import CreateNewListing

def index(response):
    ads = Ad.objects.all()
    return render(response, "main/index.html", {"ads":ads})

def new_ad(response):
    if response.method == "POST":
        form = CreateNewListing(response.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            title, price, seller = data["title"], data["price"], data["seller"]
            t = Ad(title=title, price=price, seller=response.user)
            t.save()
        
        return HttpResponseRedirect("/")
           
    else:
        form = CreateNewListing()
        
    return render(response, "main/new_ad.html", {"form":form})


