from django.contrib import admin

from . import models

admin.site.register(model_or_iterable=models.Simulation)
admin.site.register(model_or_iterable=models.Snapshot)
admin.site.register(model_or_iterable=models.Species)
admin.site.register(model_or_iterable=models.FofGroups)
