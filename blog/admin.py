from django.contrib import admin
from .models import About, Contact, Post

# Register your models here.

admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(About)
