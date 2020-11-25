from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class BlogListView(ListView):
	model = Post
	template_name = 'blog.html'
	context_object_name = 'list_blog'