from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('books/', views.books, name='books'),
    path('books/book_details/<int:id>', views.details, name='book_details'),
]
