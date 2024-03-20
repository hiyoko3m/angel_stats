from wagtail import hooks

from .views import angel_viewset


@hooks.register('register_admin_viewset')
def register_viewset():
    return angel_viewset
