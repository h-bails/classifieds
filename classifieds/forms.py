from django import forms
from .models import Advertisement
from django.contrib.auth.models import User
from cloudinary.forms import CloudinaryFileField
from django.forms import ModelForm, TextInput, EmailInput


class AdForm(forms.ModelForm):
    '''Form to create a new ad instance'''
    # auto resize the uploaded images
    image_1 = CloudinaryFileField(
        options={
            'crop': 'fill',
            'width': 800,
            'height': 800,
        },
        required=False,
    )
    image_2 = CloudinaryFileField(
        options={
            'crop': 'fill',
            'width': 800,
            'height': 800,
        },
        required=False,
    )
    # specify form fields and style the input widgets for the fields

    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price',
                  'category', 'image_1', 'image_2']
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Title of your ad...'
            }),
            'description': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'height: 7rem',
                'placeholder': 'Tell us about your amazing item(s)'
            }),
            'price': forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': '€'
            }),
            'category': forms.Select(attrs={
                'class': "form-control",
                'placeholder': '€'
            }),
        }


class ContactForm(forms.Form):
    '''Form for a potential buyer to get in touch with a seller.'''
    message = forms.CharField(widget=forms.Textarea(attrs={
                              'class': "form-control mt-3",
                              'style': 'height: 8rem',
                              'placeholder': ('Type your message to the'
                              ' seller. Your contact details will be'
                              ' automatically included in the email.')
                              }))
    fields = ['message']
