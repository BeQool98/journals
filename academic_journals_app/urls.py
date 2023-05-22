from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"), 
    path('book-details/<slug:slug>', BookDetail.as_view(), name="book_detail")
]
