from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from news.models import Category, Tag, News
from django.contrib import messages


def workspace(request):
    news = News.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        news = news.filter(
            Q(description__icontains=search_query) |
            Q(name__icontains=search_query) |
            Q(content__icontains=search_query)
        )
    return render(request, 'workspace/index.html', {'news': news})


def create_news(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        content = request.POST.get('content')
        date = request.POST.get('date')
        category_id = request.POST.get('category')
        tags = request.POST.getlist('tags')

        if category_id:
            news = News.objects.create(
                name=name,
                description=description,
                content=content,
                date=date,
                category_id=category_id
            )

        if tags:
            news.tags.add(*tags)

        image = request.FILES.get('image')

        if image:
            news.image = image
            news.save()

        messages.success(request, f'The news "{news.name}" has been created successfully.')

        return redirect('/workspace/')

    return render(request, 'workspace/create_news.html', {
        'tags': tags
    })


def update_news(request, id):
    news_object = get_object_or_404(News, id=id)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        content = request.POST.get('content')
        date = request.POST.get('date')
        category_id = request.POST.get('category')
        tags = request.POST.getlist('tags')
        image = request.FILES.get('image')

        news_object.name = name
        news_object.description = description
        news_object.content = content
        news_object.date = date
        news_object.category_id = category_id
        if image:
            news_object.image = image
        news_object.save()

        news_object.tags.clear()
        news_object.tags.add(*tags)

        messages.success(request, f'The news "{news_object.name}" has been updated successfully.')

        return redirect('/workspace/')

    return render(request, 'workspace/update_news.html', {
        'news': news_object,
        'categories': categories,
        'tags': tags
    })


def delete_news(request, id):
    news_object = get_object_or_404(News, id=id)
    news_object.delete()
    messages.warning(request, f'The news "{news_object.name}" has been deleted successfully.')
    return redirect('/workspace/')

# Create your views here.
