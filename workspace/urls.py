from django.urls import path
from . import views

urlpatterns = [
    path('create-news/', views.create_news, name='create-news'),
    path('update/<int:id>', views.update_news, name='update-news'),
    path('delete-news/<int:id>', views.delete_news, name='delete-news')
]
