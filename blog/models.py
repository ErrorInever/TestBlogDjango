from django.db import models


class StatusNews(models.IntegerChoices):
	"""Status of news"""
	DRAFT = 0, 'draft'
	PUBLISH = 1, 'publish'


class StatusPost(models.IntegerChoices):
	"""Status of post"""
	DRAFT = 0, 'draft'
	PUBLISH = 1, 'publish'


class News(models.Model):
	title = models.CharField(max_length=200)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	content = models.TextField()
	status = models.IntegerField(default=StatusNews.DRAFT, choices=StatusNews.choices)

	# TODO make author
	
	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-created_on']


class Post(models.Model):
	title = models.CharField(max_length=200)
	tagline = models.CharField(max_length=20)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	content = models.TextField()
	status = models.IntegerField(default=StatusPost.DRAFT, choices=StatusPost.choices)

	# TODO make author

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-created_on']