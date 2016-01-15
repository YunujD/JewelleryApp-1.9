import datetime
from decimal import Decimal
from django.shortcuts import render, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from registration.models import RegistrationProfile

from .form import ContactForm, ActivationForm
from Product.forms import ProductSearchForm
from Accessories.models import Material,MaterialPrice
import pprint


def home(request):
    return render(request, "home.html", {})


def about(request):
    return render(request, "about.html", {})


def homepage(request):
    if request.user.is_anonymous():  # to check if the user has logged in and isn't anonymous
        return HttpResponseRedirect("http://127.0.0.1:8000/")
    else:
        #queryset = MaterialPrice.objects.get(timestamp=str(datetime.datetime.now().date()))
        gold_obj = Material.objects.filter(name__startswith="gold").order_by('-id').first()
        if gold_obj:
            gold_id = gold_obj.id
            latest_gold_obj = MaterialPrice.objects.filter(name=gold_id).order_by('-timestamp').first()
            request.session['material_date'] = latest_gold_obj.timestamp.strftime('%Y-%m-%d T %H:%M:%S')
            request.session['gold_price'] = float(latest_gold_obj.rate)
            #print request.session.gold_price
        silver_obj = Material.objects.filter(name__startswith="silver").order_by('-id').first()
        if silver_obj:
            silver_id = silver_obj.id
            latest_silver_obj = MaterialPrice.objects.filter(name=silver_id).order_by('-timestamp').first()
            request.session['silver_price'] = float(latest_silver_obj.rate)

        #silver_id = Material.oblects.filter(name__startswith="silver")
        #gold_price = MaterialPrice.objects.()
        #request.session['material_date'] = queryset.materialDate
        ##request.session['gold_price'] = queryset.goldPrice
        #request.session['silver_price'] = queryset.silverPrice
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




