from django.shortcuts import render
from rest_framework import generics
from .models import Bucket 
from .serializers import BucketSerializer
from django.http import HttpResponse
# Create your views here.
class BucketList(generics.ListCreateAPIView):
    queryset=Bucket.objects.all()
    serializer_class=BucketSerializer

class BucketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Bucket.objects.all()
    serializer_class=BucketSerializer



def HomeView(request):
    return HttpResponse("Welcome to the Travel Bucket RESTful API!")