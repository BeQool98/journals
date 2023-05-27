from django.db import models
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

# Create your models here.

#Create your User model her if necessary
class User(models.Model):
    author = models.CharField(max_length=50)

    # class Meta:
    #     verbose_name = "User"
    #     verbose_plural = "Users"
    
    def __str__(self):
        return self.author
#Book Model

STATUS = (
    ("Draft", "Draft"),
    ("Published", "Published")
    
)



class Category(models.Model): #Category for the Article
    title = models.CharField(max_length=200) #Title of the Category
    created_on = models.DateTimeField(auto_now_add=True) #Date of creation

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

class BookDetailPost(models.Model):
    title = models.CharField(max_length=200, unique=True, help_text="The name of your book") #Title of the Article
    slug = models.SlugField(max_length=200, unique=True,help_text="Re-type the name of your book", null=True, blank=True) #Unique identifier for the article
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts',null=True, blank=True) #Author of the Article
    description = models.TextField(help_text="A short description of your book") #Short Description of the article
    quote = models.CharField(max_length=300, null=True, blank=True)
    # content = RichTextUploadingField(config_name='awesome_ckeditor') #Content of the article, you need to install CKEditor
    # tags = TaggableManager() #Tags for a Particular Article, You need to install Taggit
    category = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL,null=True, blank=True, help_text="Choose the ctegory your book fall in.") #Category of the article
    keywords = models.CharField(max_length=250, help_text="Choose keywords to locate your book easier", null=True, blank=True) #Keywords to be used in SEO
    cover = models.ImageField(upload_to='book_covers/', null=True, blank=True) #Cover Image of the article
    book = models.FileField(upload_to='books/',null=True, help_text='Upload your book here')# The book
    created_on = models.DateTimeField(auto_now_add=True) #Date of creation
    updated_on = models.DateTimeField(auto_now=True) #Date of updation
    status = models.CharField(choices=STATUS, max_length=200, default="Published") #Status of the Article either Draft or Published

    def __str__(self):
        return self.title
    
    def get_total_comments(self):
        return Comment.objects.filter(comment=self).count() 

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.slug)])

class Comment(models.Model):
    comment = models.ForeignKey(BookDetailPost, related_name="comments", help_text="Numberof comments in a post", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, help_text="Name of the person making a comment", null=True, blank=True)
    email = models.EmailField(help_text="Email of the person making a comment", null=True, blank=True)
    description = models.TextField(help_text="The comment made", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, help_text="Date created", null=True, blank=True)

    def __str__(self):
        return f"{self.comment.title} | {self.name}"

     
# from django_comments_xtd.models import XtdComment
# class MyComment(XtdComment):
#     title = models.CharField(max_length=256)
#     page = models.ForeignKey(BookDetailPost, related_name="comments", help_text="Numberof comments in a post", on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return self.title