from django.shortcuts import render,HttpResponseRedirect
from django.forms import Select
from .forms import ProductSearchForm,ProductAddForm
from .models import Product
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.

class ProductDetailView(DetailView):
	model=Product

class ProductListView(ListView):
	model=Product

	def get_queryset(self, *args,**kwargs):
		qs=super(ProductListView,self).get_queryset(*args,**kwargs)
		query=self.request.GET.get("search")
		if query:
			qs=self.model.objects.filter(
				Q(product_name__icontains=query) 
				)
		return qs


def search(request):
	product_name=None
	form=ProductSearchForm(request.POST or None)
	if form.is_valid():
		# login=form.save(commit=False)
		barcode=form.cleaned_data['barcode']
		product_exists=Product.objects.filter(barcode=barcode)
		if product_exists:
			product_name=product_exists[0]
	
	context={'search_form':form,'product_name':product_name}
	template="product_search.html"
	if request.user.is_anonymous():   # to check if the user has logged in and isn't anonymous
		return HttpResponseRedirect("http://127.0.0.1:8000/")
	else:
		return render(request,template,context)

def add(request):
	message=None
	if request.user.is_anonymous():   # to check if the user has logged in and isn't anonymous
		return HttpResponseRedirect("http://127.0.0.1:8000/")
	else:
		form=ProductAddForm(request.POST or None, request.FILES)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.image=form.cleaned_data['image']
			instance.save()
			message="Product Added"
			
		context={'add_product_form':form,'message':message}
		template="product_add.html"
		return render(request,template,context)

	

