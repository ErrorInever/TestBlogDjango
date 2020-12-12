from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Blog(models.Model):
	blog_title = models.CharField(max_length=50)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.blog_title

	def get_absolute_url(self):
		return reverse('blog', args=[str(self.id)])


class StatusPost(models.IntegerChoices):
	"""Status of post"""
	DRAFT = 0, 'draft'
	PUBLISH = 1, 'publish'


class Post(models.Model):
	title = models.CharField(max_length=200)
	tagline = models.CharField(max_length=20)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	content = models.TextField()
	status = models.IntegerField(default=StatusPost.DRAFT, choices=StatusPost.choices)
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-created_on']