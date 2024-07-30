from monitor import Manager
from constants.chats import chat_codes_aviator
from helpers.format_messages import check_strategy
from helpers.format_files import inverter_linhas_log
from telegram import TelegramClient
from datetime import datetime

manager = Manager()

old_messages = []


FILENAME = "simulator_vip.log"
CHAT_ID = chat_codes_aviator["1win_vip"]
DATE_STR = "2024-07-25"
DATE = datetime.strptime(DATE_STR, "%Y-%m-%d")

telegramClient = TelegramClient()
client = telegramClient.get_client()


# Função para obter as mensagens antigas de um grupo
async def get_old_messages():
    with open(FILENAME, "w", encoding="utf-8") as file:
        async for message in client.get_chat_history(CHAT_ID):
            # Se a data for diferente da data especificada, parar de obter mensagens
            if message.date < DATE:
                break
            try:
                if message.text is not None:
                    date = message.date.strftime("%Y-%m-%d %H:%M:%S")
                    message_text = message.text.replace("\n", "")
                    file.write(f"{date} {message_text}" + "\n")
            except Exception as e:
                print(e)
                continue


# Iniciar o cliente
with client:
    client.loop.run_until_complete(get_old_messages())
    inverter_linhas_log(FILENAME)
    check_strategy(FILENAME)
