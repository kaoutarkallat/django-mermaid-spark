from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticated, AllowAny
from django.db.utils import IntegrityError

from ..data_service import ProductService
from pprint import pprint

class ProductByIdView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, message_id):
        records = ProductService.get_by_id(message_id)
        return Response(records)

    def put(self, request, message_id):
        output = ProductService.update(message_id, request.data, return_object=True)
        return Response(output)


class ProductView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request):
        category= request.query_params.get("category",None)
        page_num= request.query_params.get("page",1)
        print('+++++++')
        print(category)
        print(page_num)
        print(int(page_num))
        if category and page_num:
            print('hello')
            records = ProductService.get_by_category_page(category,int(page_num))
            print('hi')
        else:
            records = ProductService.get_all()

        return Response(records)

    def post(self, request):
        output = ProductService.post(request.data, return_object=True)
        
        return Response(output)