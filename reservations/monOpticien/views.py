from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import  ModelViewSet as MV
from monOpticien.serializers import *
from rest_framework.response import Response
# Create your views here.
class ClientView(MV):
    serializer_class = ClienSerializer
    queryset = Client.objects.all()
    def update(self, request, pk=None):
        pass


    