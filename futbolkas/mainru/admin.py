from django.contrib import admin
from mainru.models import * 

class ItemruAdmin(admin.ModelAdmin):
	list_display =('name', 'price')

class CategoryruAdmin(admin.ModelAdmin):
	list_display=('id','name')


admin.site.register(Categoryru,CategoryruAdmin)
admin.site.register(Itemru,ItemruAdmin)
# Register your models here.
