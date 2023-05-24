from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.

def login_user(request):
    return render(request, "index.html")

def about_page(request):
    return render(request, "about_page.html")
    

class Home(ListView):
    model = BookDetailPost
    template_name= "book.html"

    def  get_context_data(self,*args, **kwargs):
        category = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["category"] = category
        return context




class BookDetail(DetailView):
    model = BookDetailPost
    template_name= "book-details.html"

   
def download(self, document_id) :
        document = get_object_or_404(BookDetailPost, pk=document_id)
        response = HttpResponse(document.book, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{document.book.name}"'
        return response





def category(request, title):
    category = Category.objects.filter(category=title)

    context = {'title': title, 'category': category}
    
    return render(request, 'category.html', context)
    #| slice: "200"
  

# def home(request):
#     book = BookDetailPost.objects.all()
#     category = Category.objects.all()

#     context = {
#         'object_list': book,
#         'category': category
#     }
#     return render(request, 'book.html', context)

# def book_detail(request, slug):
#     book = BookDetailPost.objects.filter(slug=slug)
#     book_details = BookDetailPost.objects.all()

#     context = {
#         'object': book_details
#     }

    # return render(request, 'book-details.html', context)

# def get_category(request):
#     category = Category.objects.all()
#     print('cat:', category)

#     context={
#         'category': category
#     }

#     return render(request, 'category-option.html')