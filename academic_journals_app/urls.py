from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
<<<<<<< HEAD
    # path('login/', login_user, name="login"),
    path('about/', about_page, name="about"),
    path('contact_message/', contact_message, name="contact_message"),
    path('book-details/<slug:slug>', BookDetail.as_view(), name="book_detail"),
    path('download/<int:document_id>', download, name="download"),
=======
    path('login/', login_user, name="login"),
    # path('main/', main, name="main"),
    path('about/', about_page, name="about"),
    path('book-details/<slug:slug>/', BookDetail.as_view(), name="book_detail"),
    # path('book-details/<int:pk>/comment', CommentView.as_view(), name="comment"),
    path('download/<int:document_id>/', download, name="download"),
>>>>>>> 92a0527727c195f90c720e5e11823566c050a588
    path('search/', search, name="search"),
    # path('category/', category, name="category"),
    path('category/<str:title>/', category_id, name="category_id"),

   
]

    # path('', get_category, name="get_category"),