from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeViews, name='home'),
    path('<str:groupName>/', views.indexViews, name='index')
]
