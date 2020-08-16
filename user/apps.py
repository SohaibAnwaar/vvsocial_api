from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class ProfilesConfig(AppConfig):
    name = 'user'
    verbose_name = _('user')

    def ready(self):
        import user.signals  # noqa