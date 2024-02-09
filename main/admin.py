from django.contrib import admin

from .models import Card, Word


class CardAdmin(admin.ModelAdmin):
    list_display = ['term', 'box']
    list_filter = ['box']


class WordAdmin(admin.ModelAdmin):
    pass


admin.site.register(Card, CardAdmin)
admin.site.register(Word, WordAdmin)
