
from django.contrib import admin
from .models import *
# Register your models here.

class RegisterLoss(admin.ModelAdmin):
	list_display=['loss_type_id','loss_type_name','loss_in_lal','loss_percentage']
	class Meta:
		mode=Loss

admin.site.register(Loss,RegisterLoss)


class RegisterProduct(admin.ModelAdmin):
	list_display=['product_id','product_name','product_desc','category','barcode']
	class Meta:
		mode=Product

admin.site.register(Product,RegisterProduct)

class RegisterProductStone(admin.ModelAdmin):
	list_display=['stone_type','product','quantity']
	class Meta:
		mode=ProductStone

admin.site.register(ProductStone,RegisterProductStone)

admin.site.register(Catalog)
