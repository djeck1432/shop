from django.contrib import admin
from main.models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
