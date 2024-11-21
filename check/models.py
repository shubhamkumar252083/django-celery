from django.db import models
from django.utils.timezone import now

class One(models.Model):
    name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
    
    def save(self, *args, **kwargs):
        if not self.updated_at:
            self.updated_at = now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
