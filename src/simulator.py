from helpers import get_type_message,  get_assertiveness
from monitor import Manager

FILENAME = "simulator_vip.log"
LIMIT_REDS_PER_DAY = 2
LIMIT_GREENS_PER_DAY = 1000
VALUE_BET = 10
HOUR_INITIAL = "01:00"

def write_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)

manager = Manager()
last_date = ""
reds_day = 0
greens_day = 0
total_reds = 0
total_greens = 0
assertiveness = 0
# Eu quero fazer um programa que vai mapear a hora que cada red acontece
# e a hora que cada green acontece
# e a quantidade de reds e greens por hora

map_reds = {}

# Clean file
with open("results.log", "w") as file:
    file.write("")
    

with open(FILENAME, "r") as file:
    for line in file:
        date = line[0:10]
        time = line[11:19]
        hour = line[11:13]
        message = line[19:]
        message_type = get_type_message(message)
        # if message_type == 'red':
        #     if hour in map_reds:
        #         map_reds[hour] += 1
        #     else:
        #         map_reds[hour] = 1
        assertiveness_prev = get_assertiveness(message)
        if assertiveness_prev != None:
            assertiveness = assertiveness_prev
        if time < HOUR_INITIAL:
            continue
        if last_date == "":
            last_date = date
        elif last_date != date:
            data = manager.get_data()
            result_str = f"Date -> {last_date} - RED -> {data['total_reds']} - GREEN -> {data['total_greens']}\n"
            write_file(f"results.log", result_str)
            total_greens += data["total_greens"]
            total_reds += data["total_reds"]
            # Reset data
            last_date = date
            manager.reset()
            reds_day = 0
            greens_day = 0

        if reds_day < LIMIT_REDS_PER_DAY and greens_day < LIMIT_GREENS_PER_DAY:
            # result = manager.bet_after_first_red(message, message_type, False, assertiveness)
            result = manager.bet_after_second_red(message, message_type, False, assertiveness)
            # result = manager.bet_after_third_red(
            #     message, message_type, False)
            if result == "red":
                # print(f"## Date {date}")
                # print(f"Hora: {hour} - {message}\n")
                # reds_day += 1
                if hour in map_reds:
                    map_reds[hour] += 1
                else:
                    map_reds[hour] = 1
            elif result == "green":
                greens_day += 1


print("Fim do programa")
# print(manager.show_panel(""))
print(f"Total de REDs: {total_reds}")
print(f"Total de GREENs: {total_greens}")

gain = total_greens * VALUE_BET  - (total_reds * VALUE_BET * 7)

print(f"Total de ganhos: {gain}")

print("Mapa de REDs por hora")
for key in map_reds:
    print(f"{key}, {map_reds[key]}")