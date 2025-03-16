from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']
    search_fields = ['town', 'address', 'owner']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_filter = ['new_building']
    list_editable = ['new_building']
