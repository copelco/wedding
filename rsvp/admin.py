from django.contrib import admin

from rsvp.models import Guest


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_submitted', 'party_size', 'arrival_date')
    list_filter = ('arrival_date', 'party_size')
    search_fields = ('name', 'party_size')
    ordering = ('-date_submitted',)


admin.site.register(Guest, GuestAdmin)
