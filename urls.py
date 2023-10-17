from django.urls import path 
from . import views 
from .views import BlogDestroyApi, BlogDetailApi, BlogListApi, BlogUpdateApi, BlogCreateApi

urlpatterns = [
    path('add/', BlogCreateApi.as_view(), name = "uploadBlog"), 
    path('bloglist/', BlogListApi.as_view(), name = "blog_list"), 
    path('blogUpdate/<int:pk>/', BlogUpdateApi.as_view(), name = "blog_update"), 
    path('blogdetail/<int:pk>/',BlogDetailApi.as_view(), name = "blog_detail" ),
    path('blogdelete/<int:pk>/', BlogDestroyApi.as_view(), name = "blog_delete"), 
]