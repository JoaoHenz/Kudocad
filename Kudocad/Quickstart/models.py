from django.db import models
import uuid


class Movie(models.Model):
    public_id = models.UUIDField(
        unique=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=128)
    mpaa_rating = models.CharField(max_length=32)
    budget = models.IntegerField()
    gross = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=64)
    runtime = models.IntegerField()
    rating = models.DecimalField(decimal_places=2, max_digits=6)
    rating_count = models.IntegerField()
    summary = models.CharField(max_length=1024)
