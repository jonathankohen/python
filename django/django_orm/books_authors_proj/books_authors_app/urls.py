from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_book', views.new_book),
    path('books/<int:idBook>', views.books),
    path('delete/<int:idBook>', views.delete),
    path('edit/<int:idBook>', views.edit),
    path('author_to_book/<int:idBook>', views.author_to_book),
    path('updatebook/<int:idBook>', views.update_book)
]
