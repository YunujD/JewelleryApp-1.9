from __future__ import unicode_literals
from decimal import Decimal
from django.db import models


# Create your models here.
class Type(models.Model):
    type_name = models.CharField(max_length=100, unique=True)
    def __unicode__(self):
        return self.type_name

class Category(models.Model):
    category_id = models.AutoField(primary_key=True, null=False)
    j_type = models.ForeignKey(Type)
    category_name = models.CharField(max_length=50, unique=True)
    category_desc = models.CharField(max_length=100)
    # product=models.ForeignKey(Product)

    def __unicode__(self):
        return self.category_name

    class Meta:
        unique_together = ('j_type', 'category_name')

    
class SubCategory(models.Model):
    sub_category_id = models.AutoField(primary_key=True, null=False)
    category = models.ForeignKey(Category)
    sub_category_name = models.CharField(max_length=100, unique=True)
    loss = models.DecimalField(max_digits=7,decimal_places=4,default=Decimal('0.0000'))
    manf_cost = models.DecimalField(max_digits=7,decimal_places=2,default=Decimal('0.00'))
    GOLD = 'gold'
    SILVER = 'silver'
    matetial_types = (
        (GOLD, 'GOLD'),
        (SILVER, 'SILVER'),
    )
    material = models.CharField(max_length=8,
                                choices=matetial_types,
                                default=GOLD)

    def __unicode__(self):
        return self.sub_category_name

    class Meta:
        unique_together = ('category', 'sub_category_name')


# class Tier(models.Model):
#     tier_id = models.AutoField(primary_key=True, null=False)
#     category = models.ForeignKey(Category)
#     tier_name = models.CharField(max_length=100)

#     def __unicode__(self):
#         return self.tier_name

#     class Meta:
#         unique_together = ('tier_id', 'category')