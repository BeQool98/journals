from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(User)
admin.site.register(Category)

admin.site.register(AboutHeaders) 
admin.site.register(AboutPage)
admin.site.register(EditorialMembers)
admin.site.register(ContactUs)


class BookDetailPostAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}
admin.site.register(BookDetailPost, BookDetailPostAdmin)
