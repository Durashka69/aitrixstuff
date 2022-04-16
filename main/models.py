from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


class Announcement(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Название объявления')
    description = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='pictures',
                              verbose_name='Изображение', blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    address = models.CharField(max_length=512, verbose_name='Адрес')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Время обновления')
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, verbose_name='Категория')
    subcategory = models.ForeignKey(
        'Subcategory', on_delete=models.CASCADE, verbose_name='Подкатегория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created', 'title']


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Подкатегория')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='subcategory')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
