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
        category1= request.query_params.get("category1",None)
        category2= request.query_params.get("category2",None)
        page_num= request.query_params.get("page",1)
      
        if category and page_num:
            records = ProductService.get_by_category_page(category,int(page_num))
        if category1 and category2 and page_num:
            page_num = int(page_num)
            records = ProductService.get_by_two_category_page(category1,category2,page_num)
            product1 = [p for p in records if p['type']==category1]
            product2 = [p for p in records if p['type']==category2]
            results = []
            
            i=0
            j=0
            for k in range(len(product1)+len(product2)):
                if k%2==0:
                    if i < len(product1):
                        results.append(product1[i])
                    i+=1
                if k%2==1:
                    if j < len(product2):
                        results.append(product2[j])
                    j+=1
                k+=1
            records = results[(page_num-1)*9:page_num*9]
        else:
            records = ProductService.get_all()

        return Response(records)

    def post(self, request):
        output = ProductService.post(request.data, return_object=True)
        
        return Response(output)