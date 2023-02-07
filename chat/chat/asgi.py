"""
ASGI config for chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    # 장고의 urls include와 유사한 역할 (urlpatterns를 최상위 라우터와 연결)
    # URLRouter는 path 리스트를 인자로 받습니다.
    "http" : django_asgi_app,
    "websocket": URLRouter(app.routing.websocket_urlpatterns),
})
