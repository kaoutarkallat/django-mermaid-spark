from django.db import models
from .product import Product
from django.utils import timezone

class HistoryProduct(models.Model):
    deleted = models.DateTimeField(null=True,blank=True, default=timezone.now)
    created = models.DateTimeField(null=True,blank=True, default=timezone.now)
    rank = models.IntegerField(null=True,blank=True, db_index=True)
    type = models.CharField(max_length=10000,null=True,blank=True, db_index=True, 
        choices=[
            ("accessories","accessories"),
            ("bras","bras"),
            ("leggings","leggings"),
            ("shorts","shorts"),
            ("sneakers","sneakers"),
            ("tank_tops","tank_tops")
        ])
    url = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    img_front = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    img_back = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    price = models.CharField(max_length=10000,null=True,blank=True)
    oldprice = models.CharField(max_length=10000,null=True,blank=True)
    star = models.IntegerField(blank=True,null=True,default=5)
    Reviews = models.IntegerField(null=True,blank=True, default=0)
    description = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    long_description = models.CharField(max_length=10000,null=True,blank=True)

    class Meta:
            db_table = "history_product"


