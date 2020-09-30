from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('dashboard', views.dashboard),
    path('add_item', views.add_item),
    path('create_item', views.create_item),
    path('add/<int:item_id>', views.fav_item),
    path('remove/<int:item_id>', views.unfav_item),
    path('delete_item/<int:item_id>', views.delete_item),
    path('wish_items/<int:item_id>', views.show_item),
]
