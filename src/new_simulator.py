from helpers import get_type_message, get_assertiveness
from monitor import Manager

FILENAME = "simulator_vip.log"
LIMIT_REDS_PER_DAY = 2
LIMIT_GREENS_PER_DAY = 5
HOUR_INITIAL = "09:00"
HOUR_END = "13:59"
GALE = 0
FACTOR_MULTI = 1
if GALE == 1:
    FACTOR_MULTI = 3
elif GALE == 2:
    FACTOR_MULTI = 7
# ACCURACY = 85.0 + GALE = 0
ACCURACY = 85.0


VALUE_BET = 10
WALLET = 30


def write_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)


last_date = ""
reds_day = 0
greens_day = 0
total_reds = 0
total_greens = 0
assertiveness = 0

manager = Manager()

manager.set_accuracy(ACCURACY)
# Clean file
with open("results.log", "w") as file:
    file.write("")

print("Starting simulation...\n")
with open(FILENAME, "r") as file:
    for line in file:
        if last_date == "":
            last_date = date
        date = line[0:10]
        time = line[11:19]
        if time <= HOUR_INITIAL or time >= HOUR_END:
            continue

        message = line[19:]
        message_type = get_type_message(message)
        assertiveness = get_assertiveness(message)

        if last_date != date:
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

        if reds_day >= LIMIT_REDS_PER_DAY or greens_day >= LIMIT_GREENS_PER_DAY:
            continue

        result = manager.bet_after_first_red(
            message, message_type, False, assertiveness, GALE
        )
        if result == "red":
            manager.set_stack_type_result([])
            reds_day += 1
        elif result == "green":
            greens_day += 1


total_bets = total_reds + total_greens
print(f"Total de apostas: {total_bets}")


gain = total_greens * VALUE_BET - (total_reds * VALUE_BET * FACTOR_MULTI)

print(f"Total de ganhos: R$ {gain},00")
if total_bets > 0:
    percent_greens = total_greens / (total_greens + total_reds) * 100
    # print(f"Taxa de acerto: {round(float(percent_greens))}%")

print("\nSimulation finished!")
