from pyrogram import Client
from dotenv import load_dotenv
import os
from constants.chats import chat_codes_aviator
from helpers.format_messages import check_strategy 
load_dotenv()

api_hash = os.getenv("API_HASH")
api_id = os.getenv("API_ID")
session_name = "session"
filename = "mensagens_vip.log"
chat_id = chat_codes_aviator['1win_vip']

client = Client(session_name, api_id=api_id, api_hash=api_hash)

# Função para obter as mensagens antigas de um grupo
async def get_old_messages():
    with open(filename, "w") as file:
      async for message in client.get_chat_history(chat_id, limit= 100000):
          # Agrupar toda a mensagem na mesma linha pois a message.text já vem com quebra de linha
          try:
            if message.text is not None:
              message_text = message.text.replace("\n", "")
              file.write(message_text + "\n")
          except Exception as e:
            print(e)
            continue
      
# Iniciar o cliente
with client:
    client.loop.run_until_complete(get_old_messages())
    check_strategy(filename)

# check_strategy(filename)
