from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    stream_url = models.URLField()
    cover_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
