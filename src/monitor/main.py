from pyrogram import filters
from constants.chats import chat_codes_aviator
from telegram import TelegramClient
from helpers import get_type_message
from Manager import Manager
import schedule
from services import refresh
import threading
import time

CHAT_VIP_ID = chat_codes_aviator["1win_vip"]
CHAT_ID = chat_codes_aviator["1win"]
TIME_FOR_REFRESH = 15  # minutes

telegramClient = TelegramClient()
app = telegramClient.get_client()

Manager_vip_group = Manager()
Manager_group = Manager()


# Função para monitor o grupo
@app.on_message(filters.chat(CHAT_VIP_ID) & filters.text)
def monitor_vip_group(_, message):
    message_text = message.text
    message_type = get_type_message(message_text)

    print(">>> VIP GROUP <<<")
    Manager_vip_group.show_panel(message_type=message_type)
    Manager_vip_group.bet_after_first_red(message_text, message_type)


@app.on_message(filters.chat(CHAT_ID) & filters.text)
def monitor_group(_, message):
    message_text = message.text
    message_type = get_type_message(message_text)

    print("### NORMAL GROUP ###")
    Manager_group.show_panel(message_type=message_type)
    Manager_group.bet_after_first_red(message_text, message_type)


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


schedule.every(TIME_FOR_REFRESH).minutes.do(refresh)
threading.Thread(target=run_schedule, daemon=True).start()

app.run()
