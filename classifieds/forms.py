from django import forms
from .models import Advertisement
from django.contrib.auth.models import User


class AdForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'category']


class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea)
