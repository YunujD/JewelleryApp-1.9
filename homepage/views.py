import datetime

from django.shortcuts import render, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from registration.models import RegistrationProfile

from .form import ContactForm, ActivationForm
from Product.forms import ProductSearchForm
from Accessories.models import Material



def home(request):
    return render(request, "home.html", {})


def about(request):
    print request
    return render(request, "about.html", {})


def homepage(request):
    if request.user.is_anonymous():  # to check if the user has logged in and isn't anonymous
        return HttpResponseRedirect("http://127.0.0.1:8000/")
    else:
        queryset = Material.objects.get(materialDate=str(datetime.datetime.now().date()))
        request.session['material_date'] = queryset.materialDate
        request.session['gold_price'] = queryset.goldPrice
        request.session['silver_price'] = queryset.silverPrice
        context = {'search_form': ProductSearchForm}
        return render(request, "homepage.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    title = "Contact Us"
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_full_name = form.cleaned_data.get('full_name')
        form_message = form.cleaned_data.get('message')
        subject = "Some Subject here"
        from_email = settings.EMAIL_HOST_USER
        to_email = ['youremail@gmail.com', from_email]
        message = " %s: %s via %s" % (form_full_name, form_message, form_email)
        send_mail(subject, message, from_email, to_email, fail_silently=False)
    context = {
        'contact_form': form,
        'title': title
    }
    return render(request, "forms.html", context)


def activate(request):
    form_username = None
    context = {}
    if request.user.is_anonymous():  # to check if the user has logged in and isn't anonymous
        return HttpResponseRedirect("http://127.0.0.1:8000/")
    else:
        form = ActivationForm(request.POST or None)
        if form.is_valid():
            form_username = form.cleaned_data.get('username')
        context = {
            'activate_form': form,
        }
        if form_username:
            user_instance = User.objects.get(username=form_username)
            user = RegistrationProfile.objects.get(user=user_instance)
            return HttpResponseRedirect("http://127.0.0.1:8000/accounts/activate/%s" % (user.activation_key))
        else:
            return render(request, "forms.html", context)




