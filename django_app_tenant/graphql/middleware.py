from graphene import ResolveInfo

from django_app_core.loaders import generate_loader_for_one_to_many


class DashboardLoaders:
    def __init__(self):
        from django_app_tenant.graphql.dashboard.types.contract import ContractNode
        from django_app_tenant.graphql.dashboard.types.domain import DomainNode

        self.contracts_by_tenant_loader = generate_loader_for_one_to_many(
            ContractNode, "tenant_id"
        )()
        self.domains_by_tenant_loader = generate_loader_for_one_to_many(
            DomainNode, "tenant_id"
        )()


class HQLoaders:
    def __init__(self):
        pass


class WebsiteLoaders:
    def __init__(self):
        pass


class LoaderMiddleware:
    def resolve(self, next, root, info: ResolveInfo, **args):
        if info.context.path.startswith("/dashboard/"):
            info.context.loaders = DashboardLoaders()
        elif info.context.path.startswith("/hq/"):
            info.context.loaders = HQLoaders()
        elif info.context.path.startswith("/website/"):
            info.context.loaders = WebsiteLoaders()

        return next(root, info, **args)
