from django.db import models


class News(models.Model):

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

    name = models.CharField(verbose_name='заголовок', max_length=100)
    description = models.CharField(verbose_name='краткое описание', max_length=200)
    content = models.TextField(verbose_name='контент')
    date = models.DateTimeField(verbose_name='дата добавленения')

    def __str__(self):
        return f'{self.name} - {self.date}'



# Create your models here.
