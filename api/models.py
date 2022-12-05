from django.db import models
from tree_queries.models import TreeNode

# TODO: Add tags model
# TODO: add category model


class Series(models.Model):
    key = models.CharField(null=True, max_length=255)
    title = models.CharField(max_length=255)
    podcast = models.URLField(max_length=255)
    vodcast = models.URLField(null=True, max_length=255)
    category = models.ForeignKey(
        "api.Category", on_delete=models.PROTECT, related_name="series", null=True
    )

    class Meta:
        verbose_name_plural = "Series"


class Shiur(models.Model):
    series = models.ForeignKey(
        "api.Series", on_delete=models.PROTECT, related_name="shiurim"
    )
    size = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    audio_src = models.URLField()
    video_src = models.URLField(null=True)
    track = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Shiurim"


class Category(TreeNode):
    name = models.CharField(max_length=255)
    position = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["position"]
        verbose_name_plural = "Categories"
