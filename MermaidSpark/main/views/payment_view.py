from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticated, AllowAny
from django.db.utils import IntegrityError

from ..data_service import ProductService
from pprint import pprint
from ..paypal_service import *


from datetime import datetime, timedelta

class PaymentView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request):
        category= request.query_params.get("category",None)
        return Response()
    def post(self, request):
        print(request.data)
        t1 = datetime.now()
        payment = create_payment(None)
        t2 = datetime.now()
        print(t2 -t1)
        response = authorize_payment(payment)
        
        t3 = datetime.now()
        print(t3-t2)
        return Response(response)