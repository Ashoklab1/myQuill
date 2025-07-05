    # C:\Users\ashok_wsg2ds5\my-pythonDjango1\users\apps.py

from django.apps import AppConfig

class UsersConfig(AppConfig):
        # This is the default primary key field type for models in this app.
        default_auto_field = 'django.db.models.BigAutoField'
        # This is the full Python path to your app.
        name = 'users'
        # Optional: You can add a verbose name for the app in the admin interface
        verbose_name = 'User Accounts'
    