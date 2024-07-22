from typing import TypedDict


class MapMessageType(TypedDict):
    is_attention: str
    is_opportunity: str
    is_gale: str
    is_green: str
    is_red: str


def calculate_percentage(count: int, total: int) -> float:
    return (count * 100) / total


def map_message_type(message: str) -> MapMessageType:
    is_attention = message.find("ATENÇÃO, POSSÍVEL ENTRADA") != -1
    is_opportunity = message.find("OPORTUNIDADE") != -1
    is_gale = message.find("GALE") != -1
    is_green = message.find("GREEN") != -1
    is_red = message.find("RED") != -1
    return {
        "is_attention": is_attention,
        "is_opportunity": is_opportunity,
        "is_gale": is_gale,
        "is_green": is_green,
        "is_red": is_red,
    }


def get_type_message(message: str):
    types = map_message_type(message)
    if types["is_attention"]:
        return "attention"
    elif types["is_opportunity"]:
        return "opportunity"
    elif types["is_gale"]:
        return "gale"
    elif types["is_green"]:
        return "green"
    elif types["is_red"]:
        return "red"
    else:
        return "is_unknown"


def check_is_red(message: str):
    types = map_message_type(message)
    return types["is_red"]


def check_is_green(message: str):
    types = map_message_type(message)
    return types["is_green"]


def check_strategy(filename="mensagens.txt"):
    # Quando identifica 2 reds seguidos, verifica se o próximo é green
    # Se for, adicionar mais 1 aos contador de green
    # Se não for, adicionar mais 1 aos contador de red

    count_reds = 0
    count_greens = 0

    count_greens_after_red = 0
    count_red_after_one_red = 0

    type_last_message = ""
    type_penultimate_message = ""

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:

            is_red = check_is_red(line)
            is_green = check_is_green(line)
            is_valid_message = is_red or is_green
            if is_valid_message:
                if is_red:
                    if type_last_message == "red" and type_penultimate_message == "red":
                        count_reds += 1
                    elif type_last_message == "red":
                        count_red_after_one_red += 1
                    type_penultimate_message = type_last_message
                    type_last_message = "red"

                elif is_green:
                    if type_last_message == "red" and type_penultimate_message == "red":
                        count_greens += 1
                    elif type_last_message == "red":
                        count_greens_after_red += 1
                    type_penultimate_message = type_last_message
                    type_last_message = "green"

    percentage_greens = calculate_percentage(count_greens, count_reds + count_greens)
    print(f"Reds: {count_reds}")
    print(f"Greens: {count_greens}")
    print(f"Percentage Greens: {percentage_greens}%")

    print("\n")
    percentage_greens_after_red = calculate_percentage(
        count_greens_after_red, count_greens_after_red + count_red_after_one_red
    )

    print(f"Greens after one red: {count_greens_after_red}")
    print(f"Reds after one red: {count_red_after_one_red}")
    print(f"Percentage Greens after one red: {percentage_greens_after_red}%")


def get_reference_result(message_text):
    reference_result = message_text.split("Entrar após: ")[1].split("X")[0]
    return reference_result
