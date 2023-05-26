from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('login', login_user, name="login"),
    path('about', about_page, name="about"),
    path('book-details/<slug:slug>', BookDetail.as_view(), name="book_detail"),
    path('download/<int:document_id>', download, name="download"),
    path('search/', search, name="search"),
    # path('category/', category, name="category"),
    path('category/<str:title>/', category_id, name="category_id"),
   
]

    # path('', get_category, name="get_category"),