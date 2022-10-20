from django.contrib import admin
from .models import VolunteerType


# Register your models here.
class VolunteerTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'restricted', 'requires_driver_license')


admin.site.register(VolunteerType, VolunteerTypeAdmin)
