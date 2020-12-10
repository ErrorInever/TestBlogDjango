from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import News
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class NewsListView(ListView):
	model = News
	template_name = 'news.html'
	context_object_name = 'list_news'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		last_news = News.objects.filter(status=1).order_by('-created_on')[:3]
		if last_news:
			context['latest_two_news'] = last_news[1:3]
			context['last_news'] = last_news[0]
		return context

class NewsDetailView(DetailView):
	model = News
	template_name = 'news_detail.html'
	context_object_name = 'news'


class OpenBlogLoginView(LoginView):
	template_name = 'login.html'
	form_class = AuthUserForm
	success_url = reverse_lazy('home')

	def get_success_url(self):
		return self.success_url

class OpenBlogLogOut(LogoutView):
	next_page = reverse_lazy('home')


class OpenBlogRegisterView(CreateView):
	model = User
	template = 'register.html'
	success_url = reverse_lazy('home')
	form_class = RegisterUserForm
	success_msg = 'User create successful'

	def get_success_url(self):
		return self.success_url

	def form_valid(self, form):
		form_valid = super().form_valid(form)
		username = form.cleaned_data["username"]
		password = form.cleaned_data["password"]
		aut_user = authenticate(username=username, password=password)
		login(self.request, aut_user)
		return form_valid