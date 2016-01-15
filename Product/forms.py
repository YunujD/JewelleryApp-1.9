from django import forms
from .models import Product
from django.db import models


class ProductSearchForm(forms.ModelForm):
	class Meta:
 	   model = Product
 	   fields = ['barcode']


# class ProductForm(forms.Form):
# 	Bar=forms.ModelChoiceField(queryset=Product.objects.all().order_by('product_name'))

class ProductAddForm(forms.ModelForm):
	class Meta:
	   model = Product
	   image = models.ImageField(upload_to = 'products/', default = 'products/no-img.jpg')
 	   fields = ['product_name','product_weight','product_desc','category','sub_category','material','stones','loss_type','barcode','image']