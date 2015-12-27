from django.contrib import admin

from .models import *

# Register your models here.

class RegisterMaterial(admin.ModelAdmin):
    list_display = ['material_id', 'material_name', 'date', 'price']

    class Meta:
        mode = Material


admin.site.register(Material, RegisterMaterial)