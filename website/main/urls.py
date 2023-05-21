from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("new_ad/", views.new_ad, name="new_ad"),
    path("sign_up/", views.sign_up, name="sign_up")
]



