from django.shortcuts import render

from news.models import News


def list_news(request):
    news = News.objects.all()
    return render(request, 'list_news.html', {'news': news})


def main(request):
    return render(request, 'index.html')

# Create your views here.
