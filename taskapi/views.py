from django.shortcuts import render
from rest_framework import generics
from .models import Tasks
from .serializers import TaskSerializer

# Create your views here.
class ReadCreate(generics.ListCreateAPIView):
    queryset=Tasks.objects.all()
    serializer_class= TaskSerializer

class UpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Tasks.objects.all()
    serializer_class= TaskSerializer



