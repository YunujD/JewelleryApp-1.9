from __future__ import unicode_literals

from django.db import models
from decimal import Decimal
from Category.models import Category
from Accessories.models import Material
# Create your models here.



class Loss(models.Model):
	loss_type_id=models.AutoField(primary_key=True,null=False)
	loss_type_name=models.CharField(max_length=50)
	loss_in_lal=models.CharField(max_length=100,)
	loss_percentage=models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))

	def __unicode__(self):
		return self.loss_type_name




class ProductDetail(models.Model):
	product_id=models.AutoField(primary_key=True)
	product_name=models.CharField(max_length=50, unique=True)
	product_desc=models.CharField(max_length=100)
	#category_id=models.CharField(max_length=100)
	category=models.ForeignKey(Category, related_name="Sharer")   #_id is automatically added in case of primary key
	material=models.ForeignKey(Material) 
	loss_type = models.ForeignKey(Loss)
	barcode=models.CharField(max_length=15)
	def __unicode__(self):
		return self.product_name

	class Meta:
		unique_together=('product_id','category')