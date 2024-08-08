from pyrogram import filters
from constants.chats import chat_codes_aviator
from telegram import TelegramClient
from helpers import get_type_message, get_assertiveness
from Manager import Manager
import schedule
from services import refresh
import threading
import time

CHAT_VIP_ID = chat_codes_aviator["1win_vip"]
CHAT_ID = chat_codes_aviator["1win"]
TIME_FOR_REFRESH = 20  # minutes
HOUR_INITIAL = "09:00"
HOUR_END = "13:59"
LIMIT_REDS_PER_DAY = 2
ACCURACY = 85.0
VALUE_BET = 10
HAS_BET = True
GALE = 0

telegramClient = TelegramClient()
app = telegramClient.get_client()

Manager_vip_group = Manager(
    hour_initial=HOUR_INITIAL,
    hour_end=HOUR_END,
    limit_reds_per_day=LIMIT_REDS_PER_DAY,
    gale=GALE,
)
Manager_group = Manager(
    hour_initial=HOUR_INITIAL,
    hour_end=HOUR_END,
    limit_reds_per_day=LIMIT_REDS_PER_DAY,
    gale=GALE,
)

reds_day = 0
greens_day = 0
assertiveness_vip = 0
assertiveness = 0


# Função para monitor o grupo
@app.on_message(filters.chat(CHAT_VIP_ID) & filters.text)
def monitor_vip_group(_, message):
    global reds_day, greens_day, assertiveness_vip
    Manager_vip_group.is_enable_for_bet(reds_day)

    message_text = message.text
    message_type = get_type_message(message_text)
    assertiveness_vip = get_assertiveness(message_text)

    print(">>> VIP GROUP <<<")
    Manager_vip_group.show_panel(message_type=message_type)
    result = Manager_vip_group.bet_after_first_red(
        message_text, message_type, assertiveness_vip
    )

    if result == "red":
        reds_day += 1
    elif result == "green":
        greens_day += 1


@app.on_message(filters.chat(CHAT_ID) & filters.text)
def monitor_group(_, message):
    global reds_day, greens_day, assertiveness
    Manager_group.is_enable_for_bet(reds_day)

    message_text = message.text
    message_type = get_type_message(message_text)
    assertiveness = get_assertiveness(message_text)

    print("### NORMAL GROUP ###")
    Manager_group.show_panel(message_type=message_type)
    result = Manager_vip_group.bet_after_first_red(
        message_text, message_type, assertiveness
    )
    if result == "red":
        reds_day += 1
    elif result == "green":
        greens_day += 1


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


schedule.every(TIME_FOR_REFRESH).minutes.do(refresh)
threading.Thread(target=run_schedule, daemon=True).start()

app.run()
