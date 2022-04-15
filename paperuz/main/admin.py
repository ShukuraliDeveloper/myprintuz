from django.contrib import admin
from .models import (
    Comment,
    Product,
    Category,
    Portfolio,
    Article,
    Currency,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    readonly_fields = ('currency',)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'phone',)
    search_fields = ('author',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'created',)
    search_fields = ('name', 'id',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('currency_type', 'summa')
