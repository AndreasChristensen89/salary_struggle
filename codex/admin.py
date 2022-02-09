from django.contrib import admin
from .models import Interviewer, Item


class InterviewerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'intellect',
        'coldness',
        'coding',
        'impress_lvl',
        'paid',
        'level',
    )

    ordering = ('level',)


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'charm',
        'intellect',
        'coding',
        'energy',
    )


admin.site.register(Interviewer, InterviewerAdmin)
admin.site.register(Item, ItemAdmin)
