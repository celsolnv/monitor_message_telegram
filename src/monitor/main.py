from pyrogram import filters
import requests
from constants.chats import chat_codes_aviator
from telegram import TelegramClient
from helpers import get_type_message, get_reference_result
from typing import Literal
from playsound import playsound


CHAT_ID = chat_codes_aviator["1win_vip"]

telegramClient = TelegramClient()
app = telegramClient.get_client()

HAS_REQUEST = True

MessageType = Literal["attention", "opportunity", "gale", "green", "red", "is_unknown"]
last_type_message: MessageType = "is_unknown"
penultimate_type_message: MessageType = "is_unknown"


def bet_aviator(reference: str):
    data = {"reference_result": f'{reference}x', "limit": "2"}
    res = requests.post("http://localhost:8000/bet", json=data)
    print(res.json())


# Função para monitor o grupo
@app.on_message(filters.chat(CHAT_ID) & filters.text)
def monitor_messages(_, message):
    global last_type_message, penultimate_type_message
    message_text = message.text
    message_type = get_type_message(message_text)
    # print(f"Nova mensagem no grupo: {message_text}")
    # print(f"Mapeamento: {message_type}")

    if (
        HAS_REQUEST
        and last_type_message != "is_unknown"
        and penultimate_type_message != "is_unknown"
    ):
        if (
            # last_type_message == "red"
            penultimate_type_message == "red"
            and message_type == "opportunity"
        ):
            reference = get_reference_result(message_text)
            playsound("assets/notification.wav")
            bet_aviator(reference)
    if message_type == 'red' or message_type == 'green':
        last_type_message, penultimate_type_message = message_type, last_type_message
    print(f"Último tipo de mensagem: {last_type_message}")
    print(f"Penúltimo tipo de mensagem: {penultimate_type_message}")
    print('\n')


app.run()
