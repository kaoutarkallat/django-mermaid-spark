from typing import List, Sequence
from django.contrib import admin
from django.utils.html import escape
from django.utils.safestring import mark_safe

from main.data_service.hist_product_service import HistoryProductService
from ..models import *
from django.db.models.query import QuerySet


# fields = ( 'image_tag', )
# readonly_fields = ('image_tag',)

@admin.action(description='Switch Products')
def switch(modeladmin, request, queryset:QuerySet):
    print(queryset)
    first_product:Product = queryset.first()
    last_product:Product = queryset.last()
    temp = first_product.rank
    first_product.rank = last_product.rank
    last_product.rank = temp
    first_product.save()
    last_product.save()

@admin.action(description='Move to the Top')
def move_top(modeladmin, request, queryset:QuerySet):
    
    top_product = Product.objects.exclude(rank__isnull = True).latest('rank')
    serializer = ProductSerializer(top_product)
    top_rank = serializer.data['rank']

    selected:List[Product]= queryset.all()
    for i,p in enumerate(selected):
        p.rank = top_rank + i + 1
        p.save()

    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def get_action_choices(self, request):
        choices = super(ProductAdmin, self).get_action_choices(request)
        choices.pop(0)
        choices.reverse()
        return choices


    def front(self,obj):
        return mark_safe(u'<img width="100" height="100" src="%s" />' % escape(obj.img_front))
    def back(self,obj):
        return mark_safe(u'<img width="100" height="100" src="%s" />' % escape(obj.img_back))
    def aliexpress(self,obj):
        return mark_safe(u'<a href="%s" />Aliexpress</a>' % escape(obj.url))

    search_fields = ["type","description","long_description","img_front","img_back"]
    ordering = ("-rank",)
    list_filter = ("type",)
    list_display = (
        "id",
        # "rank",
        "front",
        "back",
        "type",
        "aliexpress",
        # "img_front",
        # "img_back",
        "price",
        "oldprice",
        "star",
        "Reviews",
        "description",
        "long_description",
        # "url"   
    )
    fields = (
        "url", 
        "type",
        "img_front",
        "img_back",
        "price",
        "oldprice",
        "star",
        "Reviews",
        "description",
        "long_description",
    )
    actions = [switch, move_top]







from main.serializers.core import ProductSerializer
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

@receiver(post_save, sender=Product)
def update_rank(sender, instance, created, **kwargs):
    if created:
        top_product = Product.objects.exclude(rank__isnull = True).latest('rank')
        serializer = ProductSerializer(top_product)
        top_rank = serializer.data['rank']

        instance.rank = top_rank+1
        instance.save()

@receiver(pre_delete, sender=Product)
def save_in_history(sender, instance, **kwargs):
    serializer = ProductSerializer(instance)
    product = serializer.data
    res = HistoryProductService.post(product)
    print(res)
        
