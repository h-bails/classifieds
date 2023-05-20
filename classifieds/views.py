from django.shortcuts import render
from django.views import generic
from .models import Advertisement, Category

# Create your views here.


class AdList(generic.ListView):
    model = Advertisement
    queryset = Advertisement.objects.order_by('-posted_on')
    template_name = 'index.html'
    paginate_by = 9
