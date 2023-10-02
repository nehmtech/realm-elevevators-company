from django.contrib import admin
from .models import Category, Author, Post, Comment, Reply
from forms.models import Contact, Help

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Contact)
admin.site.register(Help)

