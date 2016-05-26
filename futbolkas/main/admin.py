from django.contrib import admin
from main.models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class PaysAdmin(admin.ModelAdmin):
    list_display = ('name', 'familiy_name', 'number', 'email', 'country', 'city', 'adress')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Forma, PaysAdmin)
