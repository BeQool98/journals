from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"), 
    path('book-details/<slug:slug>', BookDetail.as_view(), name="book_detail"),
    path('download/<int:document_id>', download, name="download"),
    path('category/<str:title>/', category, name="category"),
    # path('', get_category, name="get_category"),
]
