from django.contrib import admin

from news.models import News, Category, Tag, AdditionalInfo

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(AdditionalInfo)
# admin.site.register(NewsTags)

# Register your models here.
