from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView, UpdateView
from .models import Post, Blog
from .forms import CreatePost
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404


class CreatePost(CreateView):
	model = Post
	template_name = 'create_post.html'
	form_class = CreatePost
	success_url = reverse_lazy('home')

	def get_success_url(self):
		return reverse('blog', kwargs={'pk': self.kwargs['blog_id']})

	def form_valid(self, form, *args, **kwargs):
		blog_id = form.instance.blog_id = self.kwargs['blog_id']
		self.object = form.save(commit=False)
		self.object.blog = get_object_or_404(Blog, id=blog_id)
		self.object.save()
		return super().form_valid(form)


class PostListView(ListView):
	model = Post
	template_name = 'blog.html'
	context_object_name = 'posts_list'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		current_blog = Blog.objects.get(pk=self.kwargs['pk'])
		context['blog'] = Blog.objects.get(pk=self.kwargs['pk'])
		return context

	def get_queryset(self, **kwargs):
		return Post.objects.filter(blog__id=self.kwargs['pk'])



class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'
	context_object_name = 'post_detail'


class UpdatePostView(UpdateView):
	model = Post
	template_name = 'update_post.html'
	form_class = CreatePost

	def get_success_url(self):
		return reverse('blog', kwargs={'pk': self.kwargs['blog_id']})

	def get_context_data(self, **kwargs):
		kwargs['update'] = True
		return super().get_context_data(**kwargs)

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		return kwargs