from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync


from .models import PrivateChatRoom, PrivateRoomChatMessage

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, 
            self.channel_name
            )
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
       
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type':'chat', 
            'message':message
        }))


    def _get_room(self, id):
        return PrivateChatRoom.objects.filter(id=id).all()