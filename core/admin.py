from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_on', 'updated_on'  ,'content', 'status')
	list_filter = ('status', 'updated_on')