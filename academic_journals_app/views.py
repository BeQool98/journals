from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
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
        latest = BookDetailPost.objects.all().last()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["category"] = category
        context["latest"] = latest
        return context




class BookDetail(DetailView):
    model = BookDetailPost
    # form_class = CommentForm
    template_name= "book-details.html"
    # fields = '__all__'

    def form_valid(self, form):
         form.instance.post_id = self.kwargs['pk']
         return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
         category = Category.objects.all()  
         comment = CommentForm()
         unique_comment = Comment.objects.all()
         context= super(BookDetail, self).get_context_data(*args,**kwargs)
         context["category"] = category
         context["comment"] = comment
         context["unique_comment"] = unique_comment
         return context
    



   
def download(self, document_id) :
        document = get_object_or_404(BookDetailPost, pk=document_id)
        response = HttpResponse(document.book, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{document.book.name}"'
        return response


def category_id(request, title):
    category = Category.objects.all()
    category_id = BookDetailPost.objects.filter(category=title)
    print('cats_book:',category)

    context = { 'category_id': category_id, 'category': category }
    
    return render(request, 'category-option-id.html', context)

def search(request):
    category = Category.objects.all()

    if request.method == 'POST':
        search = request.POST.get('search_btn')
        print(search)
        searched = BookDetailPost.objects.filter(title__contains=search)
        searched_author = BookDetailPost.objects.filter(keywords__contains=search)
        print('search:', searched)
        print('s_a:', searched_author)
        latest = BookDetailPost.objects.all().last()

        context = {
             'searched': searched,
             'searched_author': searched_author,
             'latest': latest,
             'search': search,
             'category': category
        }
        return render(request, 'search.html', context)

    else:
         
        return render(request, 'search.html', {'category': category})

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