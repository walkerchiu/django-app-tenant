# django_app_tenant/apps.py

from django.apps import AppConfig


class DjangoAppTenantConfig(AppConfig):
    name = "django_app_tenant"

    def ready(self):
        pass
