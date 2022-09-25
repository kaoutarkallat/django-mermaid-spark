from asyncore import file_dispatcher
from django.db.utils import IntegrityError
from django.db import connection

from ..models import Request
from ..serializers import RequestSerializer

class RequestService:

    def get_all():
        request = Request.objects.all()
        serializer = RequestSerializer(request, many= True)
        return serializer.data

        
    
    def update(id, request_dict, return_object= False):
        request = Request.objects.get(pk = id)
        requestSerializer = RequestSerializer(request, data = request_dict, partial=True)
        msg = None
        if requestSerializer.is_valid(raise_exception=True):
            try:
                requestSerializer.save()
                print(connection.queries[-1]["sql"])
                request = requestSerializer.data
                msg = {"massage":"Request updated"}
            except IntegrityError as e: 
                print(e)
        if return_object:
            return request
        return msg

    def post(request_dict, return_object= False):
        requestSerializer = RequestSerializer(data = request_dict)
        request = None
        res = None
        if requestSerializer.is_valid(raise_exception=True):
            # request =requestSerializer.validated_data
            try:
                requestSerializer.save()
                request = requestSerializer.data
                # request = requestSerializer.validated_data
                res = {"massage":"Request saved"}
            except IntegrityError as e: 
                if 'unique constraint' in e.__str__():
                    print("Already exist")
                    res = {"message":"Request Already exists"}
                print(e)
        if return_object:
            return request
        return res

    def delete_all():
        Request.objects.all().delete()
        