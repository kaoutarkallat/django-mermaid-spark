from asyncore import file_dispatcher
from django.db.utils import IntegrityError
from django.db import connection

from ..models import Product
from ..serializers import ProductSerializer

class ProductService:

    def get_all():
        product = Product.objects.all().order_by('id')
        serializer = ProductSerializer(product, many= True)
        return serializer.data

    def get_by_category_page(category, page_num):
        product = Product.objects.filter(type = category).order_by('id')[(page_num-1)*9:page_num*9]
        serializer = ProductSerializer(product, many= True)
        return serializer.data

    def get_by_two_category_page(category1,category2,page_num):
        product = Product.objects.filter(type__in = (category1,category2)).order_by('id')
        serializer = ProductSerializer(product, many= True)
        return serializer.data
        

    def get_by_id(id):
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product)
        return serializer.data

    def get_by_zip_code(zip_code):
        result = None
        try:
            product = Product.objects.get(zip_code = zip_code)
            serializer = ProductSerializer(product)
            result = serializer.data
        except Product.DoesNotExist:
            result = None
        return result
    
    def update(id, product_dict, return_object= False):
        product = Product.objects.get(pk = id)
        productSerializer = ProductSerializer(product, data = product_dict, partial=True)
        msg = None
        if productSerializer.is_valid(raise_exception=True):
            try:
                productSerializer.save()
                print(connection.queries[-1]["sql"])
                product = productSerializer.data
                msg = {"massage":"Product updated"}
            except IntegrityError as e: 
                print(e)
        if return_object:
            return product
        return msg

    def post(product_dict, return_object= False):
        productSerializer = ProductSerializer(data = product_dict)
        product = None
        res = None
        if productSerializer.is_valid(raise_exception=True):
            # product =productSerializer.validated_data
            try:
                productSerializer.save()
                product = productSerializer.data
                # product = productSerializer.validated_data
                res = {"massage":"Product saved"}
            except IntegrityError as e: 
                if 'unique constraint' in e.__str__():
                    print("Already exist")
                    res = {"message":"Product Already exists"}
                print(e)
        if return_object:
            return product
        return res

    def delete_all():
        Product.objects.all().delete()
        