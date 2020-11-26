from django.shortcuts import render
from django.views.generic import ListView
from .models import News
from django.views.generic import TemplateView


class NewsListView(ListView):
	model = News
	template_name = 'news.html'
	context_object_name = 'list_news'