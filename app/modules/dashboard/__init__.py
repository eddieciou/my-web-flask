from .resources import Dashboard


def register_resources(api):
    api.add_resource(Dashboard, '/dashboard')
