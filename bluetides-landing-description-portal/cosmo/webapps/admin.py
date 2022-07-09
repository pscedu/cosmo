from django.contrib import admin
from . import models

admin.site.register(model_or_iterable=models.Endpoint)
admin.site.register(model_or_iterable=models.Argument)
