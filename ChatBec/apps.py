from django.apps import AppConfig


class ChatbecConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ChatBec'
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'your_app'

    def ready(self):
        import your_app.signals