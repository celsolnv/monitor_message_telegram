from playsound import playsound
from services import bet_aviator, get_value, refresh
from helpers import get_type_message, get_reference_result
from typing import Literal

MessageType = Literal["attention", "opportunity", "gale", "green", "red", "is_unknown"]


def bet_after_first_red(
    message,
    message_type: MessageType,
    last_type_message: MessageType,
    total_reds,
    total_greens,
):
    message_text = message.text
    message_type = get_type_message(message_text)

    if message_type == "opportunity" and last_type_message == "red":
        playsound("assets/notification.wav")
        reference = get_reference_result(message_text)
        if True:
            bet_aviator(reference)
    elif message_type == "red" or message_type == "green":
        if message_type == "red" and last_type_message == "red":
            total_reds += 1
        elif message_type == "green" and last_type_message == "red":
            total_greens += 1
        last_type_message = message_type


# NOT IMPLEMENTED
def bet_after_second_red(
    message,
    message_type: MessageType,
    last_type_message: MessageType,
    penultimate_type_message: MessageType,
    total_reds,
    total_greens,
):
    message_text = message.text
    message_type = get_type_message(message_text)

    if message_type == "opportunity" and last_type_message == "red":
        playsound("assets/notification.wav")
        reference = get_reference_result(message_text)
        if True:
            bet_aviator(reference)
    elif message_type == "red" or message_type == "green":
        if message_type == "red" and last_type_message == "red":
            total_reds += 1
        elif message_type == "green" and last_type_message == "red":
            total_greens += 1
        last_type_message, penultimate_type_message = message_type, last_type_message
