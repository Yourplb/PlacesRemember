from django.contrib import admin
from .models import Impressions
# Register your models here.


@admin.register(Impressions)
class ImpressionsAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'created', 'location']
    list_filter = ['author', 'title', 'created', 'location']
    search_fields = ['author', 'title', 'location']
    raw_id_fields = ['author']
    ordering = ['created']
