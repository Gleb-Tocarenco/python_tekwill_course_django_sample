from django.db import models

class FancyCat(models.Model):

    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    description = models.TextField(default='', blank=True)

    class Meta:
        ordering = ('date_added', )
