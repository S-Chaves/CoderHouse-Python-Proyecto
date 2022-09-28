from django.urls import path
from .views import create_blog_view, blog_detail_view, delete_blog

urlpatterns = [
  path('create/', create_blog_view, name='createBlog'),
  path('<int:pk>/', blog_detail_view, name='blogDetail'),
  path('delete/<int:pk>/', delete_blog, name='deleteBlog')
]