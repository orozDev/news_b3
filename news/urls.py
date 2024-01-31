from django.urls import path

from news.views import list_news, detail_news

urlpatterns = [
    path('', list_news, name='list_news'),
    path('<int:id>/', detail_news, name='detail_news'),
]