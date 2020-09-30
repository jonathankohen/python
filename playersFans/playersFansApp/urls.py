from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls)
    path("", views.index),
    path("createPlayer", views.createPlayer),
    path("players/<int:idPlayer>", views.showPlayer)
]