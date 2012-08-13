from django.contrib import admin

from rsvp.models import Guest


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'party_size', 'arrival_date')
    list_filter = ('arrival_date',)
    search_fields = ('name', 'party_size')


admin.site.register(Guest, GuestAdmin)
