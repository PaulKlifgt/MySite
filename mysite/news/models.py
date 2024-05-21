from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField('Название', max_length=40, default='Безымянный проект')
    anons = models.CharField('Анонс', max_length=200, default='Анонс')
    full_text = models.TextField('Описание')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title



