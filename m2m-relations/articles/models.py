from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Topic(models.Model):

    tag = models.CharField(max_length=50)    
    article = models.ManyToManyField('Article', through='Scope')
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.tag

class Scope(models.Model):
    
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='scopes')
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной раздел', default=False)
