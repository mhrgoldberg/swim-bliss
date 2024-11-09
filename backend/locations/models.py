from django.db import models
from django.contrib.gis.db import models as gis_models


class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    coordinates = gis_models.PointField()
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Foreign Keys
    created_by = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='locations'
    )

    class Meta:
        ordering = ['-created_at']
