from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import model_to_dict

from .models import Angel, AngelEvent

@receiver(post_save, sender=Angel)
def log_angel_events(sender, instance, created, **kwargs):
    data = model_to_dict(instance, fields=[field.name for field in instance._meta.fields])
    event = {
        'type': 'created' if created else 'edited',
        'content': data,
    }
    AngelEvent.objects.create(angel=instance, event=event)
