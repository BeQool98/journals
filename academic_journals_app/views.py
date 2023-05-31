from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib import messages


# Create your views here.
'''
def login_user(request):
    return render(request, "index.html")
'''

def about_page(request):
    
    headers=AboutHeaders.objects.get()
    about_lists=AboutPage.objects.all()
    editorial_members=EditorialMembers.objects.all()
    print("headers", headers.second_header)
    context={"headers":headers, 
             "about_lists":about_lists, 
             "editorial_members":editorial_members}
    return render(request, "about_page.html", context)

def contact_message(request):
    
    
    if request.method == "GET":
        # return HttpResponse("this method is not allowed")
        return HttpResponseRedirect('/about')
    else:
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        
        try:
            new_message=ContactUs(name=name, email=email, subject=subject, messagename=message)
            new_message.save()
            messages.success(request, "Message sent successfully")
            return HttpResponseRedirect(reverse("about"))
        except:
            messages.error(request, "Failed to send Message")
            return HttpResponseRedirect(reverse("about"))
        
        print("this is the name", name,email,subject, message)
        return HttpResponseRedirect('/about')
        



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

def search(request):
     if request.method == 'POST':
        search = request.POST.get('search_btn')
        print(search)
        searched = BookDetailPost.objects.filter(title__contains=search)
        print(searched)
     return searched
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