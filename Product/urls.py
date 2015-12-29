from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include


urlpatterns = [
    url(r'^search$', 'Product.views.search',name="productSearch"), 
    url(r'^add$', 'Product.views.add',name="productAdd"), 
   ]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
