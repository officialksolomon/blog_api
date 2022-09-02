from django.apps import AppConfig


class ApiConfig(AppConfig):
    # Implicitly connect a signal handlers decorated with @receiver.
    import api.signals
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
