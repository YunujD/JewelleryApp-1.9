from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from Product.mixin import LoginRequiredMixin
from .models import Category

# Create your views here.
