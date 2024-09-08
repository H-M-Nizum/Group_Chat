from django.urls import path
from . import consumers

websocket_urlspattern = [
    path('ws/as/<str:groupName>/', consumers.MyConsumer.as_asgi()),
]