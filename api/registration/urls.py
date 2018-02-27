from django.urls import path, include
from registration import views

urlpatterns = [
    path('', views.index, name='index'),
]
