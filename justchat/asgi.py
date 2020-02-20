"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "justchat.settings")
django.setup()
application = get_default_application()


# # z tutorialu na Heroku
# import os
# import channels.asgi

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "justchat.settings")
# channel_layer = channels.asgi.get_channel_layer()