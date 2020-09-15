
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.myachievements, name='myachievements'),
    
]