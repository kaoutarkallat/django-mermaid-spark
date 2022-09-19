from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny
from django.db.utils import IntegrityError
from ..data_service import UserService
from pprint import pprint

class UserByIdView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id):
        records = UserService.get_by_id(user_id)
        return Response(records)

    def put(self, request, user_id):
        output = UserService.update(user_id, request.data, return_object=True)
        return Response(output)
        
class UserByUsernameView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, username):
        records = UserService.get_by_username(username)
        return Response(records)

    def put(self, request, username):
        output = UserService.update(username, request.data, return_object=True)
        return Response(output)

class LastLoginAdminView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    
    def get(self, request):
        records = UserService.get_last_logins()
        return Response(records)

class LastSignupAdminView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    
    def get(self, request):
        records = UserService.get_last_signups()
        return Response(records)

class UserView(APIView):
    permission_classes = (AllowAny,)

    
    def get(self, request):
        records = UserService.get_page()
        return Response(records)

    def post(self, request):
        {'firstName': 'Hassane', 'lastName': 'Lakhloufi', 'email': 'hassanelakhloufi@live.fr', 'password': 'aaaa'}
        print(request.data)
        user={}
        user["first_name"]=request.data.get("firstName", None)
        user["last_name"]=request.data.get("lastName", None)
        user["email"]=request.data.get("email", None)
        user["password"]=request.data.get("password", None)
        output = UserService.post(user, return_object=True)
        
        return Response(output)