from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView
from .serializers import PocketSerializer
from . models import Pocket
from rest_framework import permissions
from .permissions import isUser

# Create your views here.

class PocketList(ListCreateAPIView):
    serializer_class = PocketSerializer
    queryset = Pocket.objects.all()
    permissions = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user) if self.queryset.all() else [] 

class PocketDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = PocketSerializer
    queryset = Pocket.objects.all()
    permissions = (permissions.IsAuthenticated,isUser)
    lookup_fields = "id"
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)  