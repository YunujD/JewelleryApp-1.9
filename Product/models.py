from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from decimal import Decimal
from Category.models import Category,SubCategory
from Accessories.models import StoneType
# Create your models here.


# class Catalog(models.Model):
# 	catalog_id=models.AutoField(primary_key=True)
# 	catalog_name=models.CharField(max_length=50)
# 	catalog_desc=models.CharField(max_length=50)
	# products=models.ForeignKey('Product')

	# def __init__(self,name,desc):
	# 	self.catalog_name=name
	# 	self.catalog_desc=desc
	# 	return self


# class Loss(models.Model):
# 	loss_type_id=models.AutoField(primary_key=True,null=False)
# 	loss_type_name=models.CharField(max_length=50)
# 	loss_in_lal=models.CharField(max_length=100,)
# 	loss_percentage=models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))

# 	def __unicode__(self):
# 		return self.loss_type_name



class CatalogStone(models.Model):
	stone_type = models.ForeignKey(StoneType)
	catalog = models.ForeignKey("Catalog")
	quantity = models.PositiveIntegerField(default=1)
	
	
	def calStone(self):
		return self.stone_type

	def __unicode__(self):
		return self.stone_type.Stone.name
	

class Catalog(models.Model):
	sub_cat = models.ForeignKey(SubCategory)
	catalog_name = models.CharField(max_length=50)
	catalog_desc = models.CharField(max_length=50)
	stones = models.ManyToManyField(StoneType, through=CatalogStone)
	image = models.ImageField(upload_to='products/',blank=True,null=True)
	
	def __unicode__(self):
		return self.catalog_name


class Product(models.Model):
	product_id = models.AutoField(primary_key=True)
	catalog = models.ForeignKey(Catalog)
	product_name = models.CharField(max_length=50, unique=True)
	product_weight = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	#product_desc=models.CharField(max_length=100)
	#category_id=models.CharField(max_length=100)
	# category=models.ForeignKey(Category, related_name="default_category")   #_id is automatically added in case of primary key
	# # catalog=models.ForeignKey(Catalog)
	# sub_category = models.ForeignKey(SubCategory, blank=True, null=True)
	
	#material=models.ForeignKey(Material)
	# stones = models.ManyToManyField(StoneType, through=ProductStone)
	#loss_type = models.ForeignKey(Loss, blank=True, null=True)
	image = models.ImageField(upload_to='products/',blank=True,null=True)
	barcode = models.CharField(max_length=15)

	
	def __unicode__(self):
		return self.product_name

	# class Meta:
	# 	unique_together=('product_id','category')

	def get_absolute_url(self):
		return reverse("product_detail",kwargs={"pk":self.pk})

	def add_to_cart(self):
		return "%s?item=%s&qty=1" %(reverse("cart"), self.product_id)

	def remove_from_cart(self):
		return "%s?item=%s&qty=1&delete=True" %(reverse("cart"), self.product_id)

	def get_title(self):
		return "%s" %(self.product_name)

	def calc_price(self):
		material_rate = None
		category = self.category.category_name
		material = self.material
		
		#loss_tire = self.loss_type.loss_type_name
		product_stones = ProductStone.objects.filter(product=self.product_id)
		if self.loss_type:
			loss_value = self.loss_type.loss_in_lal
		else:
			loss_value = None
		# if material.upper() == 'GOLD':
		# 	# gold_obj = Material.objects.filter(name__istartswith="gold").order_by('-id')[0]
		# 	# if gold_obj:
		# 	# 	gold_id = gold_obj.id
		# 	# 	latest_gold_obj = MaterialPrice.objects.filter(name=gold_id).order_by('-timestamp')[0]
		# 	# 	material_rate = Decimal(latest_gold_obj.rate)
		# else:
		# 	# silver_obj = Material.objects.filter(name__istartswith="silver").order_by('-id')[0]
		# 	# if silver_obj:
		# 	# 	silver_id = silver_obj.id
		# 	# 	latest_silver_obj = MaterialPrice.objects.filter(name=silver_id).order_by('-timestamp')[0]
		# 	# 	material_rate = Decimal(latest_silver_obj.rate)
			
		weight = self.product_weight
		data_dict = {}
		data_dict['category'] = category
		data_dict['material'] = material
		data_dict['stone_details'] = product_stones
		data_dict['sub_category'] = self.sub_category.sub_category_name
		data_dict['weight'] = weight
		data_dict['loss_value'] = loss_value

		total_price = 0.0
		print data_dict
		if category:
			price_array = []
			stone_total = 0
			for stone in product_stones:
				stone_price = 0.0
				stone_price = stone.quantity * stone.stone_type.Stone.rate_per_carat * stone.stone_type.weight
				stone_total += stone_price
				price_array.append(Decimal(stone_price))
			#print price_array;
			total_price = (Decimal(weight) - Decimal(loss_value)) * Decimal(material_rate) + Decimal(stone_total)
			data_dict['stone_price'] = price_array
			data_dict['stone_sum'] = stone_total
		data_dict['price'] = total_price
		#print product_stones
		# for stone in product_stones:
		# 	print stone.quantity
		# 	print stone.stone_type.Stone.rate_per_carat
		# 	print stone.stone_type.weight

		print data_dict
		return data_dict
