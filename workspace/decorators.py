from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from news.models import News


def login_required(login_url=None):
    def decorator(func):
        def inner(request, *args, **kwargs):

            if not request.user.is_authenticated:
                url = reverse('login') if login_url is None else login_url
                return redirect(url)

            return func(request, *args, **kwargs)

        return inner
    return decorator


def own_news(func):

    def inner(request, id, *args, **kwargs):
        news = get_object_or_404(News, id=id)
        if news.author != request.user:
            messages.warning(request, f'You cannot change this news ). You are not hacker)😈')
            return redirect(reverse('workspace'))
        return func(request, id, *args, **kwargs)

    return inner

