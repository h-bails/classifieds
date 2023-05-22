from django.shortcuts import render, redirect
from django.views import generic
from .models import Advertisement, Category
from .forms import AdForm
from django.contrib import messages

# Create your views here.


class AdList(generic.ListView):
    model = Advertisement
    queryset = Advertisement.objects.order_by('-posted_on')
    template_name = 'index.html'
    paginate_by = 9


def profile(request):
    return render(request, "profile.html")


def new_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            form.instance.email = request.user.email
            form.instance.username = request.user.username
            form.instance.url = "test/"
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Ad posted.")
            return redirect('/')
    form = AdForm()
    context = {
        'form': form
    }
    return render(request, 'new_ad.html', context)
