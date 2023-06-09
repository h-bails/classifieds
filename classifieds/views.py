from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from .models import Advertisement, Category
from .forms import AdForm, ContactForm
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from cloudinary import exceptions as cloudinary_exceptions


class AdList(generic.ListView):
    '''Includes a list of ads on the homepage by default'''
    model = Advertisement
    queryset = Advertisement.objects.order_by('-posted_on')
    template_name = 'index.html'
    paginate_by = 9


@login_required
def new_ad(request):
    '''Creates a new ad when the 'Create an ad' form is filled out. Checks if 
    the form is valid, and if it is, saves the ad. Returns the user to the
    homepage.'''
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)

        try:
            if form.is_valid():
                ad = form.save(commit=False)
                ad.email = request.user.email
                ad.username = request.user.username
                ad.created_by = request.user
                messages.add_message(request, messages.SUCCESS,
                                     "Ad posted.")
                ad.save()
                return redirect('/')
        except cloudinary_exceptions.Error as e:
            messages.add_message(request, messages.ERROR,
                                 f"Error when uploading image: {e}")
            return render(request, 'new_ad.html', {'form': form})

    else:
        form = AdForm()
    context = {
        'form': form
    }
    return render(request, 'new_ad.html', context)


@login_required
def view_ad(request, identifier):
    '''Shows the detail of a specific ad when a user clicks on it.'''
    ad = get_object_or_404(Advertisement, identifier=identifier)
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            message = contact_form.cleaned_data['message']
            email_subject = f'Inquiry on your ad: "{ad.title}"'
            email_body = f"""Dear {ad.created_by.username},

            {request.user.username} is interested in your item '{ad.title}'.
            You can contact them on {request.user.email} - please do not reply
            to this email directly.

            Their message is below:
            {message}

            Kind regards,

            got classifieds site
            """
            send_email(
                request,
                ad.created_by.email,
                email_subject,
                email_body
            )
            return redirect('ad_detail', identifier=ad.identifier)
    else:
        contact_form = ContactForm()

    return render(request, 'ad_detail.html', context={
        'contact_form': contact_form,
        'advertisement': ad})


@login_required
def delete_ad(request, identifier):
    '''Allows logged-in users to delete ads that they have submitted.'''
    ad = get_object_or_404(Advertisement, identifier=identifier)
    if request.user != ad.created_by:
        return render(request, '403.html', status=403)

    ad.delete()
    messages.add_message(request, messages.WARNING,
                         "Ad deleted.")
    return redirect('/')


@login_required
def edit_ad(request, identifier):
    '''Allows logged-in users to edit ads that they have submitted.'''
    ad = get_object_or_404(Advertisement, identifier=identifier)
    if request.user != ad.created_by:
        return render(request, '403.html', status=403)

    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)

        try:
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,
                                     "Ad updated.")
                return redirect(reverse('ad_detail', args=[identifier]))
        except cloudinary_exceptions.Error as e:
            messages.add_message(request, messages.ERROR,
                                 f"Error when uploading image: {e}")
            return render(request, 'edit_ad.html', {'form': form})

    form = AdForm(instance=ad)
    context = {
        'form': form
    }
    return render(request, 'edit_ad.html', context)


@login_required
def save_ad(request, identifier):
    '''Allows users to save their favourite ads to a list.'''
    ad = get_object_or_404(Advertisement, identifier=identifier)
    if request.user == ad.created_by:
        return render(request, '403.html', status=403)

    saved_ads = request.user.saved_ads.all()

    if ad not in saved_ads:
        request.user.saved_ads.add(ad)
        messages.add_message(request, messages.SUCCESS, "Ad saved.")
    else:
        request.user.saved_ads.remove(ad)
        messages.add_message(request, messages.WARNING, "Ad unsaved.")
    return redirect('ad_detail', identifier=identifier)


class Profile(LoginRequiredMixin, View):
    '''Class-based view for a user's profile. Displays ads the user has
    submitted, and a list of their saved ads.'''

    def get(self, request, *args, **kwargs):
        user_ads = request.user.user_ads.all()
        saved_ads = request.user.saved_ads.all()
        context = {
            'user_ads': user_ads,
            'saved_ads': saved_ads,
        }
        return render(request, "profile.html", context)


def send_email(request, recipient, subject, message):
    '''Sends an email when a user expresses interest in an ad.'''
    try:
        send_mail(
            subject,
            message,
            'got.classifieds@gmail.com',
            [recipient, ]
        )
        messages.add_message(request, messages.SUCCESS, "Message sent.")
    except Exception as e:
        messages.add_message(request, messages.ERROR,
                             f"Failed to send email due to: {str(e)}")
