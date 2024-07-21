from constants.chats import chat_codes_aviator
from telegram import TelegramClient
from pyrogram import filters
from helpers import map_message_type

filename = "mensagens_vip2.log"
CHAT_ID = chat_codes_aviator["1win_vip"]

telegramClient = TelegramClient()
client = telegramClient.get_client()


# Função para monitor o grupo
@client.on_message(filters.chat(CHAT_ID) & filters.text)
def monitor_messages(client, message):
    print(f"Nova mensagem no grupo: {message.text}")
    print(f"Mapeamento: {map_message_type(message.text)}")


client.run()
