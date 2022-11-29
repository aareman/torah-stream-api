from django.db import models


class Series(models.Model):
    key = models.CharField(null=True, max_length=255)
    title = models.CharField(max_length=255)
    podcast = models.URLField(max_length=255)
    vodcast = models.URLField(null=True, max_length=255)


class Shiur(models.Model):
    series = models.ForeignKey(Series, on_delete=models.PROTECT, related_name="shiurim")
    size = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    audio_src = models.URLField()
    video_src = models.URLField(null=True)
    track = models.PositiveIntegerField()
