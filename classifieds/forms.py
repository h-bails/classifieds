from django import forms
from .models import Advertisement
from django.contrib.auth.models import User


# Form to create a new ad instance.
class AdForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'category']


# Form for a potential buyer to get in touch with a seller.
class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    fields = ['message']
