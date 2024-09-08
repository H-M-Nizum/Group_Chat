from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer

class MyConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Connect websocket..", event)
        self.send({
            'type':'websocket.accept'
        })
    def websocket_receive(self, event):
        print("Received Message..", event)
        self.send({
            "type": "websocket.send",
            "text": 'recive data',
        })

    def websocket_disconnect(self, event):
        print("Disconnect websocket..", event)
        raise StopConsumer()