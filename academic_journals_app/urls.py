from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), 
    path('journal_details', views.journal_detail, name="journal_detail")
]
