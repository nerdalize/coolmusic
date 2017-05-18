from django.contrib import admin

from .models import *


class VenueAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Venue, VenueAdmin)
admin.site.register(Event, EventAdmin)
