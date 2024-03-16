from django.urls import path
from . import views

urlpatterns = [
    path('', views.workspace, name='workspace'),
    path('login/', views.login_profile, name='login'),
    path('logout/', views.logout_profile, name='logout'),
    path('register/', views.register, name='register'),
    path('create-news/', views.create_news, name='create_news'),
    path('update/<int:id>', views.update_news, name='update_news'),
    path('delete-news/<int:id>', views.delete_news, name='delete_news')
]
