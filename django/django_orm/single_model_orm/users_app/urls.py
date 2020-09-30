from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all_users', views.all_users),
    path('process', views.process)
]
