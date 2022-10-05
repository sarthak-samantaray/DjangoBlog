from django.contrib import admin

# Register your models here.

from .models import Post

#We need to register the models to see those models in admin page
admin.site.register(Post)