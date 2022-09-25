from asyncore import file_dispatcher
from django.db.utils import IntegrityError
from django.db import connection

from ..models import MyAction
from ..serializers import MyActionSerializer

class MyActionService:

    def get_all():
        myaction = MyAction.objects.all()
        serializer = MyActionSerializer(myaction, many= True)
        return serializer.data

        
    
    def update(id, myaction_dict, return_object= False):
        myaction = MyAction.objects.get(pk = id)
        myactionSerializer = MyActionSerializer(myaction, data = myaction_dict, partial=True)
        msg = None
        if myactionSerializer.is_valid(raise_exception=True):
            try:
                myactionSerializer.save()
                print(connection.queries[-1]["sql"])
                myaction = myactionSerializer.data
                msg = {"massage":"MyAction updated"}
            except IntegrityError as e: 
                print(e)
        if return_object:
            return myaction
        return msg

    def post(myaction_dict, return_object= False):
        myactionSerializer = MyActionSerializer(data = myaction_dict)
        myaction = None
        res = None
        if myactionSerializer.is_valid(raise_exception=True):
            # myaction =myactionSerializer.validated_data
            try:
                myactionSerializer.save()
                myaction = myactionSerializer.data
                # myaction = myactionSerializer.validated_data
                res = {"massage":"MyAction saved"}
            except IntegrityError as e: 
                if 'unique constraint' in e.__str__():
                    print("Already exist")
                    res = {"message":"MyAction Already exists"}
                print(e)
        if return_object:
            return myaction
        return res

    def delete_all():
        MyAction.objects.all().delete()
        