import json
from channels.generic.websocket import WebsocketConsumer


class EchoConsumer(WebsocketConsumer):
 # 웹소켓 클라이언트에서

 # text frame 으로 보내면 text_data 인자에 값이 담겨지고

 # binary data frame 으로 보내면 bytes_data 인자에 값이 담겨져 호출됩니다.
 # - ref: https: /ko.javascript.info/websocket#ref-159
    def receive(self, text_data=None, bytes_data=None):

        obj = json.loads(text_data)
        json_string = json.dumps(obj)
        self.send(json_string)
        
