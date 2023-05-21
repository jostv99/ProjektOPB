from django import forms

class CreateNewListing(forms.Form):
    title = forms.CharField(label="title", max_length=50)
    price = forms.FloatField(label="price")
    seller = forms.CharField(label="seller", max_length=50)
    


