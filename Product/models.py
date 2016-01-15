from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from decimal import Decimal
from Category.models import Category,SubCategory
from Accessories.models import Material,StoneType
# Create your models here.



class Loss(models.Model):
	loss_type_id=models.AutoField(primary_key=True,null=False)
	loss_type_name=models.CharField(max_length=50)
	loss_in_lal=models.CharField(max_length=100,)
	loss_percentage=models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))

	def __unicode__(self):
		return self.loss_type_name



class ProductStone(models.Model):
	stone_type = models.ForeignKey(StoneType)
	product = models.ForeignKey("Product")
	quantity = models.PositiveIntegerField(default=1)
	def calStone(self):
		return self.stone_type

	def __unicode__(self):
		return self.stone_type.Stone.name
	


class Product(models.Model):
	product_id=models.AutoField(primary_key=True)
	product_name=models.CharField(max_length=50, unique=True)
	product_weight = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	product_desc=models.CharField(max_length=100)
	#category_id=models.CharField(max_length=100)
	category=models.ForeignKey(Category, related_name="Sharer")   #_id is automatically added in case of primary key
	sub_category = models.ForeignKey(SubCategory, blank=True, null=True)
	material=models.ForeignKey(Material)
	stones = models.ManyToManyField(StoneType, through=ProductStone)
	loss_type = models.ForeignKey(Loss, blank=True, null=True)
	image=models.ImageField(upload_to='products/',blank=True,null=True)
	barcode=models.CharField(max_length=15)
	def __unicode__(self):
		return self.product_name

	class Meta:
		unique_together=('product_id','category')

	def get_absolute_url(self):
		return reverse("product_detail",kwargs={"pk":self.pk})

	def add_to_cart(self):
		return "%s?item=%s&qty=1" %(reverse("cart"), self.product_id)

	def remove_from_cart(self):
		return "%s?item=%s&qty=1&delete=True" %(reverse("cart"), self.product_id)

	def get_title(self):
		return "%s" %(self.product_name)
	
	def calc_price(self, request):
		category = self.category.category_name
		material = self.material.name
		#loss_tire = self.loss_type.loss_type_name
		product_stones = ProductStone.objects.filter(product=self.product_id)
		if self.loss_type:
			loss_value = self.loss_type.loss_in_lal
		else:
			loss_value = None
		if material == 'gold':
			material_rate = request.session['gold_price']
		else:
			material_rate = request.session['silver_price']
		weight = self.product_weight
		data_dict = {}
		data_dict['category'] = category
		data_dict['material'] = material
		data_dict['stone_details'] = product_stones
		data_dict['sub_category'] = self.sub_category.sub_category_name
		data_dict['weight'] = weight
		data_dict['loss_value'] = loss_value

		total_price = None
		if category == 'Jwellery Item':
			price_array = []
			stone_total = 0
			for stone in product_stones:
				stone_price = 0.00
				stone_price = stone.quantity * stone.stone_type.Stone.rate_per_carat * stone.stone_type.weight
				stone_total += stone_price
				price_array.append(float(stone_price))
			#print price_array;
			total_price = (float(weight) - float(loss_value)) * float(material_rate) + float(stone_total)
			data_dict['stone_price'] = price_array
			data_dict['stone_sum'] = stone_total
		data_dict['price'] = total_price
		#print product_stones
		# for stone in product_stones:
		# 	print stone.quantity
		# 	print stone.stone_type.Stone.rate_per_carat
		# 	print stone.stone_type.weight


		return data_dict
