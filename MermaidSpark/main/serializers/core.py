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