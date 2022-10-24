from django.contrib import admin
from .models import EventConfig


# Register your models here.
class EventConfigAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_start_date', 'event_end_date', 'buildup_start_date', 'teardown_end_date')


admin.site.register(EventConfig, EventConfigAdmin)
