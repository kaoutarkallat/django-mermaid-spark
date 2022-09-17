from asyncore import file_dispatcher
from django.db.utils import IntegrityError
from ..models import User
from ..serializers import UserSerializer
from django.db import connection
from django.db.models.query import QuerySet

class UserService:

    def get_all():
        users = User.objects.all()
        serializer = UserSerializer(users, many= True)
        return serializer.data
        
    def get_page():
        users = User.objects.all()[:100]
        serializer = UserSerializer(users, many= True)
        return serializer.data

    def get_last_logins():
        users = User.objects.all().order_by('-last_login')[:100]
        serializer = UserSerializer(users, many= True)
        return serializer.data

    def get_last_signups():
        users = User.objects.all().order_by('-date_joined')[:100]
        serializer = UserSerializer(users, many= True)
        return serializer.data
    
    def set_password(username,password):
        user:User = User.objects.get(username = username)
        user.set_password(password)
        user.save()

    def set_password_to_all(password):
        users:QuerySet = User.objects.filter(password='__pass__')
        for user in users:
            user.set_password(password)
            user.save()

    def get_by_id(id):
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user)
        return serializer.data

    def get_by_username(username):
        try:
            user = User.objects.get(username=username)
            serializer = UserSerializer(user)
            return serializer.data
        except Exception as e:
            print(e)
            return None

    def update(id, user_dict, return_object= False):
        user = User.objects.get(pk = id)
        userSerializer = UserSerializer(user, data = user_dict, partial=True)
        msg = None
        if userSerializer.is_valid(raise_exception=True):
            try:
                userSerializer.save()
                print(connection.queries[-1]["sql"])
                user = userSerializer.data
                msg = {"massage":"User updated"}
            except IntegrityError as e: 
                print(e)
        if return_object:
            return user
        return msg
        
    def delete(id):
        response = User.objects.filter(pk = id).delete()
        return response
    
    def delete_by_username(username):
        try:
            response = User.objects.filter(username = username).delete()
            return response
        except Exception as e:
            return None


    def post(user_dict=None, return_object= False):
        userSerializer = UserSerializer(data = user_dict)
        user = None
        msg = None
        if userSerializer.is_valid(raise_exception=True):
            try:
                userSerializer.save()
                user = userSerializer.data
                msg = {"massage":"User saved", 'status':'success'}
            except IntegrityError as e: 
                if 'unique constraint' in e.__str__():
                    print("Already exist")
                    msg = {"message":"User Already exists", 'status':'fail', '__error':True}
                print(e)
            except:
                msg = {"message":"error occurred", "status":'fail', '__error':True}

        if return_object:
            if user is not None:
                return user
            else:
                return msg
        return msg