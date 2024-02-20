from django.urls import path

from news.views import list_news, detail_news, list_news_by_category

urlpatterns = [
    path('', list_news, name='list_news'),
    path('news-by-category/<int:id>/', list_news_by_category, name='list_news_by_category'),
    path('<int:id>/', detail_news, name='detail_news'),
]