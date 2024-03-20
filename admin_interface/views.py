from wagtail.admin.viewsets.model import ModelViewSet
from wagtail.admin.ui import tables

from .models import Angel


class AngelViewSet(ModelViewSet):
    model = Angel
    form_fields = ['name', 'is_on_heaven']
    list_display = ["__str__", tables.UpdatedAtColumn(), 'is_on_heaven']
    list_filter = ['is_on_heaven']
    icon = 'site'
    add_to_admin_menu = True
    copy_view_enabled = False
    inspect_view_enabled = True

angel_viewset = AngelViewSet('angel')
