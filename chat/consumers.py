from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class MyConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Connect websocket..", event)

        # print("channel layer,,,", self.channel_layer) # Get Default channels layer from a project
        # print("Channels Name ,,,,", self.channel_name) # Get Default Channels Name from a project
        
        # url > views > index.html > routing > consumers
        # print group name that from routing
        self.group_name = self.scope['url_route']['kwargs']['groupName']
        print("Group Name : ", self.group_name)
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.send({
            'type':'websocket.accept'
        })
    def websocket_receive(self, event):
        print("Received Message..", event)
        async_to_sync(self.channel_layer.group_send)(self.group_name, {
            'type' : 'chat.message',
            'message' : event['text']
        })
        # self.send({
        #     "type": "websocket.send",
        #     "text": 'recive data',
        # })

    def websocket_disconnect(self, event):
        print("Disconnect websocket..", event)
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

        raise StopConsumer()

    def chat_message(self, event):
        print("client---", event)
        self.send({
            "type": "websocket.send",
            "text": event['message'],
        })