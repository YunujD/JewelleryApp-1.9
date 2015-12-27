from django.contrib import admin
from .models import *
# Register your models here.

class RegisterCustomerDetail(admin.ModelAdmin):
	list_display=['cid','name','address','mobile_number','order_id']

	class Meta:
		mode=CustomerDetail

admin.site.register(CustomerDetail,RegisterCustomerDetail)






class RegisterOrderDetail(admin.ModelAdmin):
	list_display=['order_id','cid','in_show','date','eta','delivery_date','net_amout']

	class Meta:
		mode=CustomerDetail

admin.site.register(OrderDetail,RegisterOrderDetail)