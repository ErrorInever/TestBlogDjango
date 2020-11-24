from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, News


class BlogListView(ListView):
	model = Post
	template_name = 'blog.html'
	context_object_name = 'list_blog'


class NewsListView(ListView):
	model = News
	template_name = 'index.html'
	context_object_name = 'list_news'
