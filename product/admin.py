from django.contrib import admin
from .models import Warehouse, Product, SoldProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'amount', 'add_time', 'warehouse']
    search_fields = ['name', 'description']
    list_filter = ['warehouse', 'add_time']
    ordering = ['-add_time']


@admin.register(SoldProduct)
class SoldProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'amount', 'add_time', 'warehouse']
    search_fields = ['name', 'note']
    list_filter = ['warehouse', 'add_time']
    ordering = ['-add_time']
