from __future__ import unicode_literals
from django.conf import settings
from django.db import models

from Product.models import Product
# Create your models here.


class CartItem(models.Model):
	cart = models.ForeignKey("Cart")
	item = models.ForeignKey(Product)
	quantity = models.PositiveIntegerField(default=1)
	#line item total

	def remove(self):
		return self.item.remove_from_cart()
		
	def __unicode__(self):
		return self.item.product_name




class Cart(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
	items = models.ManyToManyField(Product, through=CartItem)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __unicode__(self):
		return str(self.id)
	# user
	# items 
	# timestamp ** created
	# updated ** updated

	# subtotal price
	# taxes total
	# discounts
	# total price