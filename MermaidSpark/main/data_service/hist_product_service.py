from asyncore import file_dispatcher
from django.db.utils import IntegrityError
from django.db import connection

from ..models import HistoryProduct
from ..serializers import HistoryProductSerializer

class HistoryProductService:

    def get_all():
        hist_product = HistoryProduct.objects.all().order_by('-rank')
        serializer = HistoryProductSerializer(hist_product, many= True)
        return serializer.data

    def get_by_category_page(category, page_num):
        hist_product = HistoryProduct.objects.filter(type = category).order_by('-rank')[(page_num-1)*9:page_num*9]
        serializer = HistoryProductSerializer(hist_product, many= True)
        return serializer.data

    def get_by_two_category_page(category1,category2,page_num):
        hist_product = HistoryProduct.objects.filter(type__in = (category1,category2)).order_by('-rank')
        serializer = HistoryProductSerializer(hist_product, many= True)
        return serializer.data
        

    def get_by_id(id):
        hist_product = HistoryProduct.objects.get(pk=id)
        serializer = HistoryProductSerializer(hist_product)
        return serializer.data

    def get_by_zip_code(zip_code):
        result = None
        try:
            hist_product = HistoryProduct.objects.get(zip_code = zip_code)
            serializer = HistoryProductSerializer(hist_product)
            result = serializer.data
        except HistoryProduct.DoesNotExist:
            result = None
        return result
    
    def update(id, product_dict, return_object= False):
        hist_product = HistoryProduct.objects.get(pk = id)
        productSerializer = HistoryProductSerializer(hist_product, data = product_dict, partial=True)
        msg = None
        if productSerializer.is_valid(raise_exception=True):
            try:
                productSerializer.save()
                print(connection.queries[-1]["sql"])
                hist_product = productSerializer.data
                msg = {"massage":"HistoryProduct updated"}
            except IntegrityError as e: 
                print(e)
        if return_object:
            return hist_product
        return msg

    def post(product_dict, return_object= False):
        productSerializer = HistoryProductSerializer(data = product_dict)
        hist_product = None
        res = None
        if productSerializer.is_valid(raise_exception=True):
            # hist_product =productSerializer.validated_data
            try:
                productSerializer.save()
                hist_product = productSerializer.data
                # hist_product = productSerializer.validated_data
                res = {"massage":"HistoryProduct saved"}
            except IntegrityError as e: 
                if 'unique constraint' in e.__str__():
                    print("Already exist")
                    res = {"message":"HistoryProduct Already exists"}
                print(e)
        if return_object:
            return hist_product
        return res

    def delete_all():
        HistoryProduct.objects.all().delete()
        