from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68,min_length=6,write_only=True)

    class Meta:
        model=User
        fields = ['phone','name','password']

    def validate(self,attrs):
        phone = attrs.get('phone','')
        name = attrs.get('name','')

        if not name.isalnum():
            raise serializers.ValidationError('username should be alhpanumeric')
        if not phone.isnumeric():
            raise serializers.ValidationError('phone should be numeric')
        return attrs

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(max_length=12,min_length=3)
    password = serializers.CharField(max_length=112,min_length=2,write_only=True)
    name = serializers.CharField(max_length=225,min_length=3,read_only=True)
    tokens = serializers.CharField(max_length=225,min_length=3,read_only=True)

    class Meta:
        model = User
        fields = ['phone','name','password','tokens']
    def validate(self,attrs):
        phone = attrs.get('phone',)
        name = attrs.get('name',)
        password = attrs.get('password')

        user = auth.authenticate(phone=phone,password=password)

        if not user:
            raise AuthenticationFailed('invalid credentials')
        
        return {
            'phone':user.phone,
            'name':user.name,
            'tokens':user.tokens(),
        }
        return super().validate(attrs)  