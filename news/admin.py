from django.contrib import admin
from django.utils.safestring import mark_safe

from news.models import News, Category, Tag, AdditionalInfo


class AdditionalInfoTabularInline(admin.TabularInline):
    model = AdditionalInfo
    extra = 0


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'category', 'get_image')
    list_display_links = ('id', 'name')
    list_filter = ('category', 'tags', 'date',)
    search_fields = ('name', 'content', 'date', 'description')
    readonly_fields = ('get_full_image',)
    # filter_vertical = ('tags',)
    filter_horizontal = ('tags',)
    inlines = (AdditionalInfoTabularInline,)

    # raw_id_fields = ('category', 'tags')

    @admin.display(description='Изображение')
    def get_image(self, news: News):
        if news.image:
            return mark_safe(f'<img src="{news.image.url}" width="150px" />')
        return None

    @admin.display(description='Изображение')
    def get_full_image(self, news: News):
        if news.image:
            return mark_safe(f'<img src="{news.image.url}" width="50%" />')
        return None


class NewsStackedInline(admin.StackedInline):
    model = News


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    inlines = (NewsStackedInline,)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

# admin.site.register(AdditionalInfo)

# Register your models here.
