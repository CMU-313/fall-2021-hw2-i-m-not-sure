from mayan.apps.common.apps import MayanAppConfig
from django.utils.translation import ugettext_lazy as _

class DisplayApp(MayanAppConfig):
    app_namespace = 'display'
    app_url = 'display'
    name = 'mayan.apps.display'
    verbose_name = _('Display')

    def ready(self):
        super().ready()