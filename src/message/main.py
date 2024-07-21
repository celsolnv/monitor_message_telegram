from constants.chats import chat_codes_aviator
from helpers.format_messages import check_strategy
from telegram import TelegramClient

filename = "mensagens_vip2.log"
chat_id = chat_codes_aviator["1win_vip"]

telegramClient = TelegramClient()
client = telegramClient.get_client()


# Função para obter as mensagens antigas de um grupo
async def get_old_messages():
    with open(filename, "w") as file:
        async for message in client.get_chat_history(chat_id, limit=1000):
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
