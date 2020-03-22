from .resources import Login, Logout, Register


def register_resources(api):
    api.add_resource(Login, '/login')
    api.add_resource(Logout, '/logout')
    api.add_resource(Register, '/register')

