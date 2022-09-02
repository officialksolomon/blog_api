from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api' 
    def ready(self) -> None:
        # Implicitly connect a signal handlers decorated with @receiver.
        from api import signals
