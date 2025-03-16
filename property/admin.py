from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']
    search_fields = ['town', 'address', 'owner']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    list_editable = ['new_building']
    raw_id_fields = ('liked_by', )


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user')
    list_display = ('user', 'flat', 'created_at')
    search_fields = ('user__username', 'flat__address', 'text')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ('full_name', 'phonenumber', 'pure_phone')
    search_fields = ('full_name', 'phonenumber', 'pure_phone')
