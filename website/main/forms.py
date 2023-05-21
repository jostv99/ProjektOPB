from django import forms

class CreateNewListing(forms.Form):
    title = forms.CharField(label="title", max_length=50)
    price = forms.FloatField(label="price")

class CreateNewUser(forms.Form):
    name = forms.CharField(label="name", max_length=50)
    email = forms.CharField(label="email", max_length=50)



