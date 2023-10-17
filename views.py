from django.shortcuts import render
from .serializers import BlogSerializer
from rest_framework import generics
from .models import Blog
from rest_framework.response import Response
from rest_framework.views import APIView 

# Create your views here.
class BlogCreateApi(generics.CreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class BlogUpdateApi(generics.UpdateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class BlogDetailApi(generics.RetrieveUpdateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class BlogListApi(generics.ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class BlogDestroyApi(generics.DestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer