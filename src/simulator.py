from helpers import inverter_linhas_log, get_type_message
from monitor import Manager

FILENAME = "simulator_vip.log"

# inverter_linhas_log(FILENAME)
manager = Manager()

# vai abrir um arquivo
with open(FILENAME, "r") as file:
    for line in file:
        date = line[0:19]
        message = line[19:]
        message_type = get_type_message(message)
        # manager.show_panel(message_type=message_type)
        # manager.bet_after_first_red(message, message_type, False)
        manager.bet_after_second_red(message, message_type, False, date)
        # manager.bet_after_third_red(message, message_type, False, date)

print("Fim do programa")
print(manager.show_panel(""))
