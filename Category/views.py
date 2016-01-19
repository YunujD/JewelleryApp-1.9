from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from Product.mixin import LoginRequiredMixin
from .models import Category
from Product.templates import Product

# Create your views here.


class CategoryDetailView(LoginRequiredMixin,DetailView):
	model=Category

class CategoryListView(LoginRequiredMixin,ListView):
	model=Category
	queryset=Category.objects.all()