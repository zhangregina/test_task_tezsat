from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

# admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('title', 'description', 'image', 'created_date')
    list_filter = ('created_date', 'updated_date')
    search_fields = ('title', 'description')


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'image', 'created_date')
#     list_filter = ('created_date', 'updated_date')
#     search_fields = ('title', 'description')
#
#
# admin.site.register(ProductAdmin)