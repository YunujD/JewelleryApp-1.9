from django import forms

from .models import CustomerDetail


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerDetail
        fields = ('cust_mobile_number', 'first_name', 'middle_name', 'last_name', 'address', 'gender')