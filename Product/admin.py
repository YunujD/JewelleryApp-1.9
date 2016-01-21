
from django.contrib import admin
from .models import *
# Register your models here.

# class RegisterLoss(admin.ModelAdmin):
# 	list_display=['loss_type_id','loss_type_name','loss_in_lal','loss_percentage']
# 	class Meta:
# 		mode=Loss

# admin.site.register(Loss,RegisterLoss)
class RegisterCatalog(admin.ModelAdmin):
	list_display = ['sub_cat','catalog_name','catalog_desc']
	class Meta:
		mode = Catalog

admin.site.register(Catalog,RegisterCatalog)


class RegisterProduct(admin.ModelAdmin):
	list_display = ['product_id','product_name','barcode']
	class Meta:
		mode = Product

admin.site.register(Product,RegisterProduct)

class RegisterCatalogStone(admin.ModelAdmin):
	list_display = ['catalog','stone_type','quantity']
	class Meta:
		mode = CatalogStone

admin.site.register(CatalogStone,RegisterCatalogStone)

#admin.site.register(Catalog)
