from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'

    # override the ready method to ensure signals are accessible by django when the application is ready
    def ready(self):
        import users.signals
