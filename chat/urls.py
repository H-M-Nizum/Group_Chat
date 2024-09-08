from django.urls import path
from . import views

urlpatterns = [
    path('<str:groupName>/', views.home, name='home')
]
