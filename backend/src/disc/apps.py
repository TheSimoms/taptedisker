from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DiscConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'disc'
    verbose_name = _('disc')
