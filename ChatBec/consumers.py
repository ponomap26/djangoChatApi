import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Chat

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.chat_group_name = f'chat_{self.chat_id}'

        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = await self.save_message(data)

        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'id': message.id,
            'text': message.text,
            'sender': {
                'id': message.sender.id,
                'username': message.sender.username
            },
            'receiver': {
                'id': message.receiver.id,
                'username': message.receiver.username
            },
            'chat': message.chat.id,
            'created_at': message.created_at.isoformat()
        }))

    async def save_message(self, data):
        message = Chat.objects.create(
            text=data['text'],
            sender_id=data['sender'],
            receiver_id=data['receiver'],
            chat_id=data['chat']
        )
        return message