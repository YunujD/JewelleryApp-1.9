from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Material(models.Model):
    material_id = models.AutoField(primary_key=True, null=False)
    material_name = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    price = models.IntegerField()

    def __unicode__(self):
        return self.material_name


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
