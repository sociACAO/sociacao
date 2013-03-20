from django.contrib import admin
from .models import Action, Venue


class VenueAdmin(admin.StackedInline):
    model = Venue
    extra = 1


class ActionAdmin(admin.ModelAdmin):
    inlines = (VenueAdmin, )

admin.site.register(Action, ActionAdmin)
