"""JewelleryApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
import Product
from carts.views import CartView
urlpatterns = [
 	url(r'^$', 'homepage.views.home',name="home"), 
    url(r'^home/$', 'homepage.views.homepage',name="homepage"), 
 	url(r'^contact/$', 'homepage.views.contact',name="contact"), 
    url(r'^activate/$', 'homepage.views.activate',name="activate"), 
    url(r'^about/$', 'homepage.views.about',name="about"),
    
    url(r'^products/', include('Product.urls')), 
    url(r'^admin/', admin.site.urls,name="admin"),

    #from django registration redux
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^cart/$', CartView.as_view(), name='cart'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
