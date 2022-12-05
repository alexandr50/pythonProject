from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Содержание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Categories', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    
    class Meta:
        verbose_name='Женщины'
        verbose_name_plural='Женщины'
        ordering = ['created_at', 'title']



class Categories(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='название')
    slug = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='URL')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories', kwargs={'cat_slug': self.slug})
    
    class Meta:
        verbose_name='Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']