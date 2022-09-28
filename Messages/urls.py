from django.urls import path
from .views import messages_view, send_message

urlpatterns = [
  path('<str:username>/', messages_view, name='messages'),
  path('send/<str:username>/', send_message, name='sendMessage')
]