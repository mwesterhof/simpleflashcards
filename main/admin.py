from django.contrib import admin

from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ['term', 'box']
    list_filter = ['box']


admin.site.register(Card, CardAdmin)
