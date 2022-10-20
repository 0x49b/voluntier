from django.db import models


# Create your models here.
class VolunteerType(models.Model):
    class Meta:
        verbose_name = "Volunteer Type"
        verbose_name_plural = "Volunter Types"

    name = models.CharField(max_length=50)
    restricted = models.IntegerField()
    description = models.TextField()
    requires_driver_license = models.BooleanField()

    def __str__(self):
        return self.name
