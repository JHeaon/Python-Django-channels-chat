from django.urls import path
from app.consumers import EchoConsumer

# 장고의 urls urlpatterns와 유사한 역할 (URL에 매핑)
# 장고 기본의 urls.py urlpatterns 와 다르게
# 이는 장고에서 찾아서 읽어가는 것이 아니라, 우리가 asgi.py 직접 임포트하여 지정하기에
# 다른 이름이어도 상관없습니다.

websocket_urlpatterns = [
    path("ws/echo/", EchoConsumer.as_asgi()),
]