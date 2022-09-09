from lib2to3.pgen2 import token
from django.shortcuts import render

# Create your views here.
class SignUpView(APIView):
    permission_classes= (AllowAny,)
    def post(self, request):
        output = SingUpservicw.signup(request.data, return_object=False)
        if output['status']== 200:
            token= LoginService.login(request, 'corvette2020')
            output['jwt_token']= token.get('token', None)
            if output['jwt_token'] is None:
                output['status']= 421
                output['message'] = 'wrong credentials'
                return Response(output)