from django.shortcuts import render
from django.views.generic import ListView
from .models import News


class NewsListView(ListView):
	model = News
	template_name = 'index.html'
	context_object_name = 'list_news'