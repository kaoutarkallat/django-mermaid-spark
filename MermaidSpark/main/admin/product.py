from typing import Sequence
from django.contrib import admin
from django.utils.html import escape
from django.utils.safestring import mark_safe
from ..models import *

# def view_birth_date(self, obj):
#         return obj.img_front
# image_tag.short_description = 'Image'
# image_tag.allow_tags = True
# and in your admin.py add:

# fields = ( 'image_tag', )
# readonly_fields = ('image_tag',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def front(self,obj):
        return mark_safe(u'<img width="100" height="100" src="%s" />' % escape(obj.img_front))
    def back(self,obj):
        return mark_safe(u'<img width="100" height="100" src="%s" />' % escape(obj.img_back))
    search_fields = ["type","description","long_description","img_front","img_back"]
    list_filter = ("type",)
    list_display = (
        "id",
        "front",
        "back",
        "type",
        "description",
        "img_front",
        "img_back",
        "price",
        "oldprice",
        "star",
        "Reviews",
        "long_description",
        "url"
        
    )