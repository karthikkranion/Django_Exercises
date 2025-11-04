try:
    from django.apps import AppConfig # type: ignore
except Exception:
    # Fallback minimal AppConfig so editors or environments without Django don't error.
    class AppConfig:
        pass


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
