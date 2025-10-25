from django.urls import path, include 
from . import views
  
urlpatterns = [
    path('adTask', views.addTask, name='addTask'),
]