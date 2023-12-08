from django.contrib import admin

from django_app_tenant.models import Contract, Domain, Tenant

admin.site.register(Contract)
admin.site.register(Domain)
admin.site.register(Tenant)
