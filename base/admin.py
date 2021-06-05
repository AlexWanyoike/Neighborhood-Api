from django.contrib import admin
from .models import  Neighborhood, User, Business, Post

admin.site.register(Neighborhood)
admin.site.register(User)
admin.site.register(Business)
admin.site.register(Post)