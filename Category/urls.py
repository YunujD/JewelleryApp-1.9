from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include

from .views import CategoryDetailView,CategoryListView

urlpatterns = [
    url(r'^$',CategoryListView.as_view(),name='category_list'),
    url(r'^(?P<pk>\d+)/$',CategoryDetailView.as_view(),name='category_detail'),
   ]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



