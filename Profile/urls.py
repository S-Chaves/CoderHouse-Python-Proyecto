from django.urls import path
from .views import profile_view, edit_profile_view

urlpatterns = [
  path('edit/', edit_profile_view, name='editProfile'),
  path('<str:username>/', profile_view, name='profile')
]