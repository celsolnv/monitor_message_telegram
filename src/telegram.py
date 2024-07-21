from pyrogram import Client
from dotenv import load_dotenv
import os

load_dotenv()


class TelegramClient:
    def __init__(self):
        self.api_id = os.getenv("API_ID")
        self.api_hash = os.getenv("API_HASH")
        self.client = Client(
            session_string="anon", api_id=self.api_id, api_hash=self.api_hash
        )
        # self.client.start()

    def get_chat_history(self, chat_id, limit):
        return self.client.get_chat_history(chat_id, limit)

    def get_client(self):
        return self.client
