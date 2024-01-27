from django.contrib import admin

from news.models import News, Category

admin.site.register(News)
admin.site.register(Category)

# Register your models here.
