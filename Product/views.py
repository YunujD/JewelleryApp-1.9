from django.shortcuts import render
from django.forms import Select
from .forms import ProductForm
from .models import ProductDetail
# Create your views here.


def search(request):
	productBarCode=None
	form=ProductForm(request.POST or None)
	if form.is_valid():
		# login=form.save(commit=False)
		product_name=form.cleaned_data['search']
		product_exists=ProductDetail.objects.filter(product_name=product_name)
		print product_exists
		if product_exists:
			productBarCode=product_exists[0].barcode
	
	context={'search_form':form,'productBarCode':productBarCode}
	template="product_search.html"
	return render(request,template,context)
