from django import forms
from .models import Advertisement
from django.contrib.auth.models import User
from cloudinary.forms import CloudinaryFileField


# Form to create a new ad instance.
class AdForm(forms.ModelForm):
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

    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price',
                  'category', 'image_1', 'image_2']


# Form for a potential buyer to get in touch with a seller.
class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    fields = ['message']
