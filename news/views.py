from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from news.models import News, Category
from django.core.paginator import Paginator


def list_news(request):
    news = News.objects.all()
    search_query = request.GET.get('search')

    if search_query:
        news = news.filter(
            Q(description__icontains=search_query) |
            Q(name__icontains=search_query) |
            Q(content__icontains=search_query)
        )

    paginator = Paginator(news, 2)
    page = int(request.GET.get('page', 1))
    news = paginator.get_page(page)

    return render(request, 'list_news.html', {'news': news})


def main(request):
    return render(request, 'index.html')


def list_news_by_category(request, id):
    # try:
    #     category = Category.objects.get(id=id)
    # except Category.DoesNotExist:
    #     return redirect('/news/')
    category = get_object_or_404(Category, id=id)
    news = News.objects.filter(category=category)

    search_query = request.GET.get('search')
    if search_query:
        news = news.filter(
            Q(description__icontains=search_query) |
            Q(name__icontains=search_query) |
            Q(content__icontains=search_query)
        )

    return render(request, 'list_news.html', {
        'news': news,
        'category': category
    })


def detail_news(request, id):
    news = News.objects.get(id=id)
    return render(request, 'detail_news.html', {'news': news})

# Create your views here.
