from django.db import models


class StatusNews(models.IntegerChoices):
	"""Status of news"""
	DRAFT = 0, 'draft'
	PUBLISH = 1, 'publish'


class News(models.Model):
	title = models.CharField(max_length=200)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	content = models.TextField()
	status = models.IntegerField(default=StatusNews.DRAFT, choices=StatusNews.choices)

	# TODO make author
	def get_absolute_url(self):
		return f"/news/{self.id}"

	
	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-created_on']