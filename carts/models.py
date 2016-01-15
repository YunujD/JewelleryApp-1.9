from __future__ import unicode_literals
from decimal import Decimal
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from Product.models import Product
# Create your models here.


class CartItem(models.Model):
	cart = models.ForeignKey("Cart")
	item = models.ForeignKey(Product)
	quantity = models.PositiveIntegerField(default=1)
	itemPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	line_item_total = models.DecimalField(max_digits=10, decimal_places=2)

	def remove(self):
		return self.item.remove_from_cart()
		
	def __unicode__(self):
		return self.item.product_name


def cart_item_pre_save_reciever(sender, instance, *args, **kwargs):
	qty = instance.quantity
	price = instance.item.calc_price()
	
	instance.itemPrice = Decimal(price['price'])
	line_item_total = Decimal(qty) * Decimal(price['price'])
	instance.line_item_total = line_item_total
pre_save.connect(cart_item_pre_save_reciever, sender=CartItem)

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