import asyncio
from pyrogram import Client
from dotenv import load_dotenv
import os

def discovery_chat_id(session_name = 'session'):
  api_hash = os.getenv("API_HASH")
  api_id = os.getenv("API_ID")
  async def main():
      async with Client(session_name, api_id, api_hash) as app:
          async for dialog in app.get_dialogs():
              print(dialog.chat.title or dialog.chat.first_name)
              print(dialog.chat.id)


  asyncio.run(main())

discovery_chat_id()