from django.shortcuts import render

from news.models import News


def list_news(request):
    news = News.objects.all()
    return render(request, 'list_news.html', {'news': news})


def main(request):
    return render(request, 'index.html')


def detail_news(request, id):
    news = News.objects.get(id=id)
    return render(request, 'detail_news.html', {'news': news})

# Create your views here.
