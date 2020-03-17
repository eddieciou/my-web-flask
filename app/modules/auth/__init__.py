from .resources import Login


def register_resources(api):
    api.add_resource(Login, '/login')
