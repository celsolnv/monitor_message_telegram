from pyrogram import Client
from dotenv import load_dotenv
import os
from constants.chats import chat_codes_aviator, template_aviator_message
from helpers.format_messages import check_strategy 
load_dotenv()

api_hash = os.getenv("API_HASH")
api_id = os.getenv("API_ID")
session_name = "session"
filename = "mensagens_vip.txt"

client = Client(session_name, api_id=api_id, api_hash=api_hash)

# Função para obter as mensagens antigas de um grupo
async def get_old_messages():
    with open("mensagens_vip.txt", "w") as file:
      async for message in client.get_chat_history(chat_codes_aviator['1win_vip'], limit= 10000):
          # Agrupar toda a mensagem na mesma linha pois a message.text já vem com quebra de linha

          if message.text is not None:
            message_text = message.text.replace("\n", "")
            file.write(message_text + "\n")
      
# Iniciar o cliente
# with client:
#     client.loop.run_until_complete(get_old_messages())
#     check_strategy()

check_strategy(filename)
