import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .utils.chat import chatbot_response  # Import chatbot logic

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # Get chatbot response
        response = chatbot_response(message)

        # Send response back
        await self.send(text_data=json.dumps({
            'message': response
        }))
