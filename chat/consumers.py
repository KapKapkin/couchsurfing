import json

from django.core import serializers

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async

from .models import PrivateChatRoom, PrivateRoomChatMessage, PrivateChatRoomMessageManager


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        room = text_data_json['room']
        user = text_data_json['user']

        deserialized_room = self.deserialize_obj(room)
        deserialized_user = self.deserialize_obj(user)

        await self._save_message(user=deserialized_user, room=deserialized_room, message=message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user,
            }
        ) 

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        await self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'user': user
        }))

    def deserialize_obj(self, obj):
        deserialized_obj = serializers.deserialize('json', obj)
        for obj in deserialized_obj:
            return obj.object

    @sync_to_async
    def _save_message(self, user, room, message):
        PrivateRoomChatMessage.objects.create(user=user, room=room, content=message)
