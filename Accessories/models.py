from __future__ import unicode_literals

import datetime
from decimal import Decimal
from django.db import models


# class Material(models.Model):
#     name = models.CharField(max_length=50, unique=True)

#     def __unicode__(self):
#         return self.name


# class MaterialPrice(models.Model):
#     name = models.ForeignKey(Material)
#     rate = models.DecimalField(decimal_places=2, max_digits=20,default=Decimal('0.00'))
#     timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add = False, auto_now=True)

#     def __unicode__(self):
#         return self.name.name
        

class Stone(models.Model):
    name = models.CharField(max_length=50, unique=True)
    rate_per_carat = models.DecimalField(decimal_places=2, max_digits=20,default=Decimal('0.00'))
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)
	
    def __unicode__(self):

        return self.name


class StoneType(models.Model):
    StoneType_id = models.AutoField(primary_key=True, null=False)
    Stone = models.ForeignKey(Stone)
    size = models.DecimalField(decimal_places=2, max_digits=20)
    weight = models.DecimalField(decimal_places=2, max_digits=20)

    def __unicode__(self):
        return "%s-%s mm"%(self.Stone.name, self.size)

    class Meta:
        unique_together = ('StoneType_id', 'Stone')


class MaterialRate(models.Model):
    gRate = models.DecimalField(decimal_places=2, max_digits=10,default=Decimal('0.00'))
    sRate = models.DecimalField(decimal_places=2, max_digits=10,default=Decimal('0.00'))
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)

    def __unicode__(self):
        return "%s 's Rate"%(self.timestamp)

# class Stone(models.Model):
# stone_id=models.AutoField(primary_key=True,null=False)
# 	stone_name=models.CharField(max_length=100, unique=True)
# 	price_per_carat=models.IntegerField(max_length=50)

# 	def __unicode__(self):
# 		return self.stone_name

# def StoneType(models.Model):
# 	stone_type_id=models.AutoField(primary_key=True,null=False)
# 	stone_name=models.CharField(max_length=100, unique=True)
# 	price_per_carat=models.IntegerField(max_length=50)
