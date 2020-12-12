from django.contrib import admin
from .models import Blog, Post

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	pass

@admin.register(Post)
class PostBlogAdmin(admin.ModelAdmin):
	pass
