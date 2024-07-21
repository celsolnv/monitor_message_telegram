from pyrogram import filters
from constants.chats import chat_codes_aviator
from telegram import TelegramClient
from helpers import map_message_type

FILENAME = "mensagens_vip2.log"
CHAT_ID = chat_codes_aviator["1win_vip"]

telegramClient = TelegramClient()
app = telegramClient.get_client()


# Função para monitor o grupo
@app.on_message(filters.chat(CHAT_ID) & filters.text)
def monitor_messages(_, message):
    print(f"Nova mensagem no grupo: {message.text}")
    print(f"Mapeamento: {map_message_type(message.text)}")


app.run()
