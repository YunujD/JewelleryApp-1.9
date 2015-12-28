from django.shortcuts import render,HttpResponseRedirect
from django.forms import Select
from .forms import ProductSearchForm
from .models import ProductDetail
# Create your views here.


def search(request):
	product_name=None
	form=ProductSearchForm(request.POST or None)
	if form.is_valid():
		# login=form.save(commit=False)
		barcode=form.cleaned_data['barcode']
		product_exists=ProductDetail.objects.filter(barcode=barcode)
		if product_exists:
			product_name=product_exists[0]
	
	context={'search_form':form,'product_name':product_name}
	template="product_search.html"
	if request.user.is_anonymous():   # to check if the user has logged in and isn't anonymous
		return HttpResponseRedirect("http://127.0.0.1:8000/")
	else:
		return render(request,template,context)

	
