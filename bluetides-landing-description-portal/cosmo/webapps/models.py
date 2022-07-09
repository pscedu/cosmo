from django.db import models


# Create your models here.
class Argument(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    restriction = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Endpoint(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    arguments = models.ManyToManyField(Argument, blank=True)

    def __str__(self):
        return self.name
