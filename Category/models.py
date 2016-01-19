from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True, null=False)
    category_name = models.CharField(max_length=50, unique=True)
    category_desc = models.CharField(max_length=100)
    # product=models.ForeignKey(Product)

    def __unicode__(self):
        return self.category_name

    class Meta:
        unique_together = ('category_id', 'category_name')

    def get_absolute_url(self):
        return reverse("category_detail",kwargs={"pk":self.pk})

class SubCategory(models.Model):
    sub_category_id = models.AutoField(primary_key=True, null=False)
    category = models.ForeignKey(Category)
    sub_category_name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.sub_category_name

    class Meta:
        unique_together = ('sub_category_id', 'category')


class Tier(models.Model):
    tier_id = models.AutoField(primary_key=True, null=False)
    category = models.ForeignKey(Category)
    tier_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.tier_name

    class Meta:
        unique_together = ('tier_id', 'category')