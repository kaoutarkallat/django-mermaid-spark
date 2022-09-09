class SignUpService:
    def singup(signup_data:dict, return_object= False):
        user_dict['is_superuser']= False
        user_dict['is_staff'] = False
        user_dict['is_active']= True
        user_dict['userneme']= signup_data.get('phone', None)
        user_dict['password']= 'corvette2020'
        user_dict['email']= signup_data.get('email', '_@gmail.com')
        user_dict['first_name']= signup_data.get('first_name','_')
        user_dict['last_name']= signup_data.get('last_name','_')