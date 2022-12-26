from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from djangoql.admin import DjangoQLSearchMixin

from api import models

# Register your models here.
# TODO: add a interface to setup and process shiurim
# TODO: ⭐ typeahead widget
# TODO: ⭐ Bulk edit shiurim in a category
# TODO: Add speaker admin
# TODO: setup dragable ordering https://github.com/jrief/django-admin-sortable2


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


@admin.register(models.Shiur)
class ShiurAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    search_fields = ("title", "series__title")
    filter_horizontal = ("categories",)
    list_display = ("title", "view_series", "created_at", "shiur_audio")

    def shiur_audio(self, obj):
        return format_html(
            '<audio controls style="height:18px;" src="{}"/>', obj.audio_src
        )

    def view_series(self, obj):
        url = (
            reverse("admin:api_series_changelist")
            + "?"
            + urlencode({"series__id": f"{obj.series_id}"})
        )
        return format_html('<a href="{}">{}</a>', url, obj.series)

    # NOTE: Actions
    # TODO: Add bulk change of series
    # I think we need to keep in mind the following feature set
    # 1. intermediate form page (see https://www.willandskill.se/en/articles/custom-django-admin-actions-with-an-intermediate-page)
    # 2. Add an auto order/append/prepend to series
    actions = [
        "add_categories",
    ]

    def add_categories(self, request, queryset):
        if "apply" in request.POST:
            for shiur in queryset.all():
                for id in request.POST.getlist("categories"):
                    shiur.categories.add(id)
                shiur.save()
            self.message_user(request, "Added Categories")
            return HttpResponseRedirect(request.get_full_path())

        select = forms.ModelMultipleChoiceField(
            queryset=models.Category.objects.all(),
            widget=FilteredSelectMultiple("verbose name", is_stacked=False),
        )
        return render(
            request,
            "admin/shiur_category_intermediate.html",
            context={
                "select": select.widget.render("categories", None),
                "shiurim": queryset.all(),
            },
        )


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "view_shiurim")
    list_filter = ("parent",)

    def view_shiurim(self, obj):
        total_shiurim = sum(
            [c.shiur_set.count() for c in obj.descendants(include_self=True)]
        )

        url = (
            reverse("admin:api_shiur_changelist")
            + "?"
            + urlencode(
                {
                    "categories__in": ",".join(
                        [str(c.id) for c in obj.descendants(include_self=True)]
                    )
                }
            )
        )
        return format_html('<a href="{}">{} Shiurim</a>', url, total_shiurim)
