from django.urls import path
from . import views

urlpatterns = [
    path('', views.workspace, name='workspace'),
    path('create-news/', views.create_news, name='create_news'),
    path('update/<int:id>', views.update_news, name='update_news'),
    path('delete-news/<int:id>', views.delete_news, name='delete_news')
]
