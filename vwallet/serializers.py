from django.forms import SlugField
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Pocket
from authentication.models import User

class PocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pocket
        fields = ['name','quantity','status']


class UserSerializer(serializers.ModelSerializer):

    pockets = PocketSerializer(many=True)

    class Meta:
        model = User
        fields = ['user','phone','pockets']