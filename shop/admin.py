from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """ Product class for the admin """
    
    list_display = (
        'name',
        'description',
        'price',
    )

    ordering = ('price',)

admin.site.register(Product, ProductAdmin)