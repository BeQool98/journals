from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(User)
admin.site.register(Category)

class BookDetailPostAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}
admin.site.register(BookDetailPost, BookDetailPostAdmin)

admin.site.register(Comment)
admin.site.register(Owner_Details) 
admin.site.register(Comment_Email) 

