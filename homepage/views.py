from django.shortcuts import render, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from .form import ContactForm
# Create your views here.
def homepage(request):
	if request.user.is_anonymous():   # to check if the user has logged in and isn't anonymous
		return HttpResponseRedirect("http://127.0.0.1:8000/")
	else:
		return render(request,"homepage.html",{})




def contact(request):
	form = ContactForm(request.POST or None)
	title="Contact Us"
	if form.is_valid():
		form_email=form.cleaned_data.get('email')
		form_full_name=form.cleaned_data.get('full_name')
		form_message=form.cleaned_data.get('message')
		subject="Some Subject here"
		from_email=settings.EMAIL_HOST_USER
		to_email=['youremail@gmail.com',from_email]
		message=" %s: %s via %s" %(form_full_name,form_message,form_email)
		send_mail(subject,message,from_email,to_email,fail_silently=False)
	context={
		'form':form,
		'title':title
	}
	return render(request,"forms.html",context)


def home(request):
	return render(request,"home.html",{})

def about(request):
	return render(request,"about.html",{})