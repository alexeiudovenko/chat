import json

from django.shortcuts import get_object_or_404

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import Message, Topic


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['pk']
        self.room_group_name = f'chat_{self.room_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        message = json.loads(text_data)

        new_message = await self.create_chat_message(message)
        
        data = {
            'sender_name' : 'Anonymous' if new_message.anonymous else new_message.sender_name.username,
            'text' : new_message.text,
            'date_time' : new_message.date_time.strftime("%b, %d, %Y %I:%M %p"),
        }

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': data
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def create_chat_message(self, text):
        return Message.objects.create(
            topic_message=get_object_or_404(Topic, pk=text['topic_id']),
            sender_name=self.scope['user'],
            text=text['message'],
            anonymous=text['checkbox_anon'],
        )