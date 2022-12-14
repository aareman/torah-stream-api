from django.db import models
from tree_queries.models import TreeNode

# TODO: Add tags model


class Series(models.Model):
    key = models.CharField(null=True, max_length=255)
    title = models.CharField(max_length=255)
    podcast = models.URLField(null=True, blank=True, max_length=255)
    vodcast = models.URLField(null=True, blank=True, max_length=255)
    category = models.ForeignKey(
        "api.Category", on_delete=models.PROTECT, related_name="series", null=True
    )
    is_legacy = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.category or 'Uncategorize'})"

    class Meta:
        verbose_name_plural = "Series"


class Shiur(models.Model):
    series = models.ForeignKey(
        "api.Series", on_delete=models.PROTECT, related_name="shiurim"
    )
    categories = models.ManyToManyField("api.Category")
    speaker = models.ForeignKey(
        "api.Speaker", on_delete=models.PROTECT, null=True, blank=True
    )
    size = models.PositiveIntegerField(null=True)
    title = models.CharField(max_length=255)
    audio_src = models.URLField()
    video_src = models.URLField(null=True, blank=True)
    position = models.PositiveIntegerField(null=True, default=0)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    # For tracking original imports
    imported_series = models.ForeignKey(
        "api.Series", on_delete=models.PROTECT, null=True
    )
    imported_title = models.CharField(max_length=255, null=True)

    @property
    def category(self):
        return self.series.category if self.series.category else ""

    def __str__(self):
        return self.title + f"({self.category})"

    class Meta:
        verbose_name_plural = "Shiurim"
        ordering = ["position", "created_at"]


class Category(TreeNode):
    name = models.CharField(max_length=255)
    position = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["position"]
        verbose_name_plural = "Categories"


class Speaker(models.Model):
    name = models.CharField(max_length=255)
