from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class AngelPage(Page):
    name = models.CharField(max_length=250)
    is_on_heaven = models.BooleanField()

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('is_on_heaven'),
    ]
