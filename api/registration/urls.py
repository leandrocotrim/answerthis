from django.urls import path, include
from registration import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add')
]
