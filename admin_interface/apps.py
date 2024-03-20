from django.apps import AppConfig


class AdminInterfaceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "admin_interface"

    def ready(self):
        from . import signals
