from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chatbot/$', ChatConsumer.as_asgi()),
]
