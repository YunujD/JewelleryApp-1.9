from __future__ import unicode_literals

from django.db import models

# Create your models here.


'''class OrderDetail(models.Model):
    order_id = models.AutoField(primary_key=True, max_length=50)
    cust_mobile_number = models.IntegerField(max_length=50)
    in_show = models.CharField(max_length=10, )
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    eta = models.CharField(max_length=100)
    delivery_date = models.IntegerField()
    net_amount = models.IntegerField()

    def __unicode__(self):
        return str(self.order_id)

    class Meta:
        unique_together = ('cust_mobile_number', 'order_id')
'''


class CustomerDetail(models.Model):
    cust_mobile_number = models.CharField(primary_key=True, max_length=15, default='+977-')
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    def __unicode__(self):
        return self.cust_mobile_number


