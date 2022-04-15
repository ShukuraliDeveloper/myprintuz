from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField('Имя', max_length=150)
    photo = models.ImageField('Фото', upload_to='category/img')
    description = models.TextField('Описание')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Currency(models.Model):
    class Currency_Type(models.TextChoices):
        DOL = 'долларов', _('долларов')
        EUR = 'евро', _('евро')
        RUB = 'рубль', _('рубль')

    currency_type = models.CharField('валюта', max_length=100, choices=Currency_Type.choices)
    summa = models.PositiveBigIntegerField('UZS')

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    name = models.CharField('Имя',max_length=150)
    photo = models.ImageField('Фото',upload_to='media/img')
    description = models.TextField('Описание')
    price_dol = models.PositiveBigIntegerField('Цена')
    format = models.CharField('Формат',max_length=100)
    density = models.CharField('Плотность',max_length=100)
    currency = models.PositiveIntegerField('Валюта',null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукта'


class Comment(models.Model):
    author = models.CharField('Автор',max_length=100)
    phone = models.CharField('Телефон',max_length=13)
    text = models.TextField('Текст')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Portfolio(models.Model):
    name = models.CharField('Имя',max_length=100)
    photo = models.ImageField('Фото',upload_to='media/img')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Портфолио'


class Article(models.Model):
    title = models.CharField('заглавие',max_length=100)
    photo = models.ImageField('Фото',upload_to='articles/img')
    description = models.TextField('Описание')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
