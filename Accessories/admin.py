from django.contrib import admin

from .models import *

# Register your models here.

# class RegisterMaterial(admin.ModelAdmin):
#     list_display = ['name']

#     class Meta:
#         mode = Material


# admin.site.register(Material, RegisterMaterial)
# class RegisterMaterialPrice(admin.ModelAdmin):
#     list_display = ['name','rate', 'timestamp']

#     class Meta:
#         mode = MaterialPrice


# admin.site.register(MaterialPrice, RegisterMaterialPrice)

class RegisterStone(admin.ModelAdmin):
    list_display = ['name', 'rate_per_carat']

    class Meta:
        mode = Stone


admin.site.register(Stone, RegisterStone)

class RegisterStoneType(admin.ModelAdmin):
    list_display = ['__unicode__', 'size' , 'weight']

    class Meta:
        mode = StoneType


admin.site.register(StoneType, RegisterStoneType)


class RegisterRate(admin.ModelAdmin):
    list_display = ['timestamp','sRate', 'gRate']

    class Meta:
        mode = MaterialRate


admin.site.register(MaterialRate, RegisterRate)