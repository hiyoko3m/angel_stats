from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class Angel(models.Model):
    name = models.CharField(max_length=250)
    is_on_heaven = models.BooleanField()

    def __str__(self):
        return self.name


class AngelEvent(models.Model):
    angel = models.ForeignKey(Angel, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    event = models.JSONField()
