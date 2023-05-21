from django.shortcuts import render, redirect
from .forms import Sign_upForm

# Create your views here.

def sign_up(response):
    if response.method == "POST":
        form = Sign_upForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = Sign_upForm()
        
    return render(response, "sign_up/sign_up.html", {"form":form})

