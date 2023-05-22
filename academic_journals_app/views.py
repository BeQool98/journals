from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.

class Home(ListView):
    model = BookDetailPost
    template_name= "book.html"


class BookDetail(DetailView):
    model = BookDetailPost
    template_name= "book-details.html"

# def home(request):
#     return render(request, )

# def journal_detail(request):
#     return render(request, 'blog-details.html')