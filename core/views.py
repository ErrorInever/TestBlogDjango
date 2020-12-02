from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News
from django.views.generic import TemplateView


class NewsListView(ListView):
	model = News
	template_name = 'news.html'
	context_object_name = 'list_news'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		last_news = News.objects.filter(status=1).order_by('-created_on')[:3]
		context['latest_two_news'] = last_news[1:3]
		context['last_news'] = last_news[0]
		return context

class NewsDetailView(DetailView):
	model = News
	template_name = 'news_detail.html'
	context_object_name = 'news'