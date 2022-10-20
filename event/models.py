from django.db import models


class EventConfig(models.Model):
    class Meta:
        verbose_name = "Event Config"
        verbose_name_plural = "Event Configs"

    event_name = models.CharField(max_length=255)
    buildup_start_date = models.DateField(blank=True)
    event_start_date = models.DateField(blank=True)
    event_end_date = models.DateField(blank=True)
    teardown_end_date = models.DateField(blank=True)
    event_welcome_message = models.CharField(max_length=255, blank=True, null=True)
