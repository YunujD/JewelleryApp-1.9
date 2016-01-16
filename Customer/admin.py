from django.contrib import admin

from .models import *

# Register your models here.


class RegisterCustomerDetail(admin.ModelAdmin):
    list_display = ['cust_mobile_number', 'first_name', 'middle_name', 'last_name', 'address', 'gender']

    class Meta:
        mode = CustomerDetail


admin.site.register(CustomerDetail, RegisterCustomerDetail)

'''class RegisterOrderDetail(admin.ModelAdmi	):
	list_display=['order_idid'cid','in_show','date','eta','delivery_date','net_amout	]

	class Me		:
		mode=CustomerDetail

admin.site.register(OrderDetail,RegisterOrderDet)'''