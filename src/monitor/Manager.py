from playsound import playsound
from helpers import get_type_message, get_reference_result
from services import bet_aviator, get_value, refresh


class Manager:
    def __init__(self):
        self.last_type_message = "is_unknown"
        self.penultimate_type_message = "is_unknown"
        self.third_to_last_type_message = "is_unknown"
        self.total_reds = 0
        self.total_greens = 0
        self.path_sound = "assets/notification.wav"

    def show_panel(
        self,
        message_type,
    ):
        print(f"Mensagem atual: {message_type}")
        print(f"Último tipo de mensagem: {self.last_type_message}")
        print(f"Penúltimo tipo de mensagem: {self.penultimate_type_message}")
        print("#" * 20)
        print(f"REDS: {self.total_reds}")
        print(f"GREENS: {self.total_greens}")
        print("\n")

    def get_data(self):
        return {
            "last_type_message": self.last_type_message,
            "penultimate_type_message": self.penultimate_type_message,
            "total_reds": self.total_reds,
            "total_greens": self.total_greens,
        }

    def __play_sound(self):
        playsound(self.path_sound)

    def __bet(self, message_text):
        reference = get_reference_result(message_text)
        bet_aviator(reference)

    def bet_after_first_red(self, message_text, message_type, has_bet=True):
        if message_type == "opportunity" and self.last_type_message == "red":
            if has_bet:
                self.__play_sound()
                self.__bet(message_text)
        elif message_type == "red" or message_type == "green":
            if message_type == "red" and self.last_type_message == "red":
                self.total_reds += 1
            elif message_type == "green" and self.last_type_message == "red":
                self.total_greens += 1
            self.last_type_message = message_type

    def bet_after_second_red(self, message_text, message_type, has_bet=True, date=""):
        if (
            message_type == "opportunity"
            and self.penultimate_type_message == "red"
            and self.last_type_message == "red"
        ):
            if has_bet:
                self.__play_sound()
                self.__bet(message_text)
        elif message_type == "red" or message_type == "green":
            if (
                message_type == "red"
                and self.last_type_message == "red"
                and self.penultimate_type_message == "red"
            ):
                print(date)
                print(message_text)
                self.total_reds += 1
            elif (
                message_type == "green"
                and self.last_type_message == "red"
                and self.penultimate_type_message == "red"
            ):
                self.total_greens += 1
            self.last_type_message, self.penultimate_type_message = (
                message_type,
                self.last_type_message,
            )

    def bet_after_third_red(self, message_text, message_type, has_bet=True, date=""):
        if (
            message_type == "opportunity"
            and self.penultimate_type_message == "red"
            and self.last_type_message == "red"
            and self.third_to_last_type_message == "red"
        ):
            if has_bet:
                self.__play_sound()
                self.__bet(message_text)
        elif message_type == "red" or message_type == "green":
            if (
                message_type == "red"
                and self.last_type_message == "red"
                and self.penultimate_type_message == "red"
                and self.third_to_last_type_message == "red"
            ):
                print(date)
                print(message_text)
                self.total_reds += 1
            elif (
                message_type == "green"
                and self.last_type_message == "red"
                and self.penultimate_type_message == "red"
                and self.third_to_last_type_message == "red"
            ):
                self.total_greens += 1
            (
                self.last_type_message,
                self.penultimate_type_message,
                self.third_to_last_type_message,
            ) = (
                message_type,
                self.last_type_message,
                self.penultimate_type_message,
            )
