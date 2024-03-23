from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from news.models import News


@receiver(post_save, sender=News)
def pre_save_news(sender, instance, created, **kwargs):
    if created:
        id = instance.id
        instance.name = f'{id}. {instance.name}'
        instance.save()