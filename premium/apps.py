from django.apps import AppConfig


class PremiumConfig(AppConfig):
    """
    overrides ready() and import signals
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'premium'

    def ready(self):
        import premium.signals
