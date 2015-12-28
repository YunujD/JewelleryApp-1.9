from django import forms
from .models import ProductDetail


class ProductSearchForm(forms.ModelForm):
	class Meta:
 	   model = ProductDetail
 	   fields = ['barcode']


# class ProductForm(forms.Form):
# 	Bar=forms.ModelChoiceField(queryset=ProductDetail.objects.all().order_by('product_name'))

