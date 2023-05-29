from django.shortcuts import render, redirect, get_object_or_404
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
            form.instance.user_id = request.user.id
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


def view_ad(request, identifier):
    ad = get_object_or_404(Advertisement, identifier=identifier)
    return render(request, "ad_detail.html", context={"advertisement": ad})


def delete_ad(request, identifier):
    ad = get_object_or_404(Advertisement, identifier=identifier)
    ad.delete()
    messages.add_message(request, messages.ERROR,
                         "Ad deleted.")
    return redirect('/')


def edit_ad(request, identifier):
    ad = get_object_or_404(Advertisement, identifier=identifier)
    if request.method == 'POST':
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Ad updated.")
            return redirect('/')
    form = AdForm(instance=ad)
    context = {
        'form': form
    }
    return render(request, 'edit_ad.html', context)
