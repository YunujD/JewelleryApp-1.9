from django.contrib import admin
from .models import *

# Register your models here.

class RegisterCategoryDetail(admin.ModelAdmin):
	list_display=['category_id','category_name','category_desc']

	class Meta:
		mode=Category

admin.site.register(Category,RegisterCategoryDetail)


class RegisterSubCategoryDetail(admin.ModelAdmin):
	list_display=['sub_category_id','category','sub_category_name']

	class Meta:
		mode=SubCategory

admin.site.register(SubCategory,RegisterSubCategoryDetail)

class RegisterTierDetail(admin.ModelAdmin):
	list_display=['tier_id','category','tier_name']

	class Meta:
		mode=Tier

admin.site.register(Tier,RegisterTierDetail)
