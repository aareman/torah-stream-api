from django.contrib import admin

from api import models

# Register your models here.
# TODO: add a interface to setup and process shiurim
# TODO: ⭐ typeahead widget
# TODO: ⭐ Bulk edit shiurim in a series


admin.site.register(models.Series)
admin.site.register(models.Shiur)
