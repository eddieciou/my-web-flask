from .resources import Login, Logout


def register_resources(api):
    api.add_resource(Login, '/login')
    api.add_resource(Logout, '/logout')
