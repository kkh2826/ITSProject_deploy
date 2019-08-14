from django.apps import AppConfig


class ItsappConfig(AppConfig):
    name = 'itsapp'

    def ready(self):
        import users.signals