from django.db import models

# Create your models here.

class Movie (models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    year = models.SmallIntegerField()
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)