from django import forms

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