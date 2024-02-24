from django.urls import path

from . import views

urlpatterns = [
    path('news-by-category/<int:id>/', views.list_news_by_category, name='list_news_by_category'),
    path('<int:id>/', views.detail_news, name='detail_news'),
    path('', views.list_news, name='list_news'),
]