from __future__ import unicode_literals

from django.db import models

# Create your models here.


class OrderDetail(models.Model):
    order_id = models.AutoField(primary_key=True, max_length=50)
    cid = models.CharField(max_length=50)
    in_show = models.CharField(max_length=10, )
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    eta = models.CharField(max_length=100)
    delivery_date = models.IntegerField()
    net_amout = models.IntegerField()

    def __unicode__(self):
        return str(self.order_id)

    class Meta:
        unique_together = ('cid', 'order_id')


class CustomerDetail(models.Model):
    cid = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    order_id = models.ForeignKey(OrderDetail, related_name="OrderForCustomer")


    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('cid', 'order_id')


