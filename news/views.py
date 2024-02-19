from django.shortcuts import render
from django.shortcuts import get_object_or_404

from news.models import News,Category


def list_news(request):
    news = News.objects.all()
    categories = Category.objects.all()

    selected_category_id = request.GET.get('category')

    if selected_category_id:
        news = news.filter(category__id=selected_category_id)

    search_query = request.GET.get('search')

    if search_query:
        news = news.filter(name__icontains=search_query)

    return render(request, 'list_news.html', {'news': news,'categories':categories})

def main(request):
    return render(request, 'index.html')


def detail_news(request, id):
    news = News.objects.get(id=id)
    return render(request, 'detail_news.html', {'news': news})

# Create your views here.
