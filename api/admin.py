from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from api import models

# Register your models here.
# TODO: add a interface to setup and process shiurim
# TODO: ⭐ typeahead widget
# TODO: ⭐ Bulk edit shiurim in a series


@admin.register(models.Series)
class SeriesAdmin(admin.ModelAdmin):
    fields = ("title", "podcast", "vodcast", "category")
    list_filter = ("category",)
    list_display = ("title", "category", "percent_categorized", "is_legacy")

    def percent_categorized(self, obj):
        shiurim = obj.shiurim.all()
        url = (
            reverse("admin:api_shiur_changelist")
            + "?"
            + urlencode({"series__id": f"{obj.id}"})
        )
        count = shiurim.count()
        count_categorized = shiurim.exclude(
            series__category__name="Uncategorized"
        ).count()
        return format_html(
            '<a href="{}">{} Shiurim ({})</a>',
            url,
            count,
            f"{100*(count_categorized / count) if count > 0 else 0:.2f}%",
        )


# TODO: allow playing audo from list page for cateogorization
# can have it pop out into a new window
@admin.register(models.Shiur)
class ShiurAdmin(admin.ModelAdmin):
    list_display = ("title", "view_series", "created_at", "updated_at")
    # TODO: Add bulk change of series
    # I think we need to keep in mind the following feature set
    # 1. intermediate form page (see https://www.willandskill.se/en/articles/custom-django-admin-actions-with-an-intermediate-page)
    # 2. Add an auto order/append/prepend to series
    actions = [
        "update_series",
    ]

    def view_series(self, obj):
        url = (
            reverse("admin:api_series_changelist")
            + "?"
            + urlencode({"series__id": f"{obj.series_id}"})
        )
        return format_html('<a href="{}">{}</a>', url, obj.series)

    def update_series(self, request, queryset):
        pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")
    list_filter = ("parent",)
