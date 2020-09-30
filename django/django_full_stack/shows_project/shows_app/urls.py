from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('shows', views.shows),
    path('shows/new', views.index),
    path('shows/create', views.create),
    path('shows/<int:idShow>', views.single_show),
    path('shows/<int:idShow>/edit', views.edit),
    path('shows/<int:idShow>/delete', views.delete),
    path('shows/<int:idShow>/update', views.update),

]
