from rest_framework import serializers
from .models import User

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
