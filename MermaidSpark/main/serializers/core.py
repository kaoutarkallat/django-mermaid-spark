from dataclasses import field
from rest_framework import serializers

from ..models import *

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = User
        fields = ( "id",
            "last_login","is_superuser","username","first_name","last_name",
            "email","is_staff","is_active","date_joined",'password',
        )
    def create(self, validated_data):
        user = User(**validated_data)
        # Hash the user's password.
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 
            "id",
            "created",
            "rank",
            "type",
            "url",
            "img_front",
            "img_back",
            "price",
            "oldprice",
            "description",
            "star",
            "Reviews",
            "long_description"
        )

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ( 
            'created',
            'username',
            'REQUEST_METHOD',
            'PATH_INFO',
            'QUERY_STRING',
            'REMOTE_ADDR',
            'CONTENT_TYPE',
            'HTTP_HOST',
            'HTTP_CONNECTION',
            'HTTP_CACHE_CONTROL',
            'HTTP_SEC_CH_UA',
            'HTTP_SEC_CH_UA_MOBILE',
            'HTTP_SEC_CH_UA_PLATFORM',
            'HTTP_UPGRADE_INSECURE_REQUESTS',
            'HTTP_USER_AGENT'
        )

class HistoryProductSerializer(ProductSerializer):
    class Meta:
        model = HistoryProduct
        fields = ProductSerializer.Meta.fields +('deleted',)