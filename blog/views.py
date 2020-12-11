from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import Post, Blog
from .forms import CreatePost
from django.urls import reverse_lazy

class BlogDetailView(DetailView):
	model = Blog
	template_name = 'blog.html'
	context_object_name = 'blog'


class CreatePost(CreateView):
	model = Post
	template_name = 'create_post.html'
	form_class = CreatePost
	success_url = reverse_lazy('blog')