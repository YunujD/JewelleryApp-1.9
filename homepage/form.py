from django import forms
from registration.models import RegistrationProfile

class ContactForm(forms.Form):
	full_name=forms.CharField(required=False)
	email=forms.EmailField()
	message=forms.CharField()

	def clean_email(self):
		email=self.cleaned_data.get('email')
		email_base,provider=email.split("@")
		domain,extension=provider.split('.')
		if not extension=='gmail':
			raise forms.ValidationError("Please give proper .edu extension")
		return email

class ActivationForm(forms.Form):
	username=forms.ModelChoiceField(queryset=RegistrationProfile.objects.all().order_by('user'))
	