from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import *
from django.core.paginator import Paginator, PageNotAnInteger
# from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
# Create your views here.


def login_user(request):
    return render(request, "index.html")

def about_page(request):
    return render(request, "about_page.html")


    

class Home(ListView):
    model = BookDetailPost
    template_name= "book.html"
    # paginate_by = 100
    # context_object_name = 'book_page'  # Default: object_list
    # queryset = BookDetailPost.objects.all().order_by('-created_on')  # Default: Model.objects.all()
    
    
    

    def  get_context_data(self,*args, **kwargs):
        queryset2=BookDetailPost.objects.all().order_by('-created_on')
        category = Category.objects.all() 
        BookDetailPost_list = BookDetailPost.objects.all()
        page = self.request.GET.get('page', 1)

        print('newqueryset:',self.queryset)

        new_query=[]
        new_query2= list(new_query[:2])
        for i in queryset2:  
            new_query.append(i)

        

        print('ne', list(new_query[:2]))
        print(new_query2)
            # print('item', new_query)
        
        # for i in new_query:
        #     if new_query.index(i)<2:
        #         new_query2.append(i)
        #         print("last two", i)
           

        paginator = Paginator(BookDetailPost_list, 1)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        # latest = BookDetailPost.objects.all().last()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["category"] = category
        context["book_page"] = pages 
        context["new_query"] = new_query2
        return context



class BookDetail(DetailView):
    model = BookDetailPost
    # form_class = CommentForm
    template_name= "book-details.html"
    # fields = '__all__'

    def get_context_data(self, *args, **kwargs):
         category = Category.objects.all()  
         comment_form = CommentForm()
         unique_comment = Comment.objects.filter(comment=self.get_object()).order_by('-date_created')
         context= super(BookDetail, self).get_context_data(*args,**kwargs)
         context["category"] = category
         context["comment_form" ] = comment_form
         context["unique_comment"] = unique_comment
         return context
    
    def post(self, request, *args, **kwargs):
        new_comment = Comment(description=request.POST.get('description'), comment=self.get_object(), name=request.POST.get('name'), email=request.POST.get('email'))
        new_comment.save()
        return self.get(self, request, *args, **kwargs)



   
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