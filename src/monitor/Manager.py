from playsound import playsound
from helpers import get_type_message, get_reference_result
from services import bet_aviator, get_value, refresh


class Manager:
    def __init__(self):
        self.total_reds = 0
        self.total_greens = 0
        self.path_sound = "assets/notification.wav"
        self.stack_type_result = []

    def reset(self):
        self.total_reds = 0
        self.total_greens = 0
        self.stack_type_result = []

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
        last = self.stack_type_result[-1] if len(self.stack_type_result) > 0 else ""
        penultimate = (
            self.stack_type_result[-2] if len(self.stack_type_result) > 1 else ""
        )
        return {
            "last_type_message": last,
            "penultimate_type_message": penultimate,
            "total_reds": self.total_reds,
            "total_greens": self.total_greens,
        }

    def __play_sound(self):
        playsound(self.path_sound)

    def __bet(self, message_text):
        reference = get_reference_result(message_text)
        bet_aviator(reference)

    def bet_after_first_red(self, message_text, message_type, has_bet=True, assertiveness=0):
        if assertiveness < 70.0:
            return
        result = ""
        last = self.stack_type_result[-1] if len(self.stack_type_result) > 0 else ""
        is_valid_result = message_type == "red" or message_type == "green"
        if last == "red":
            if message_type == "opportunity":
                if has_bet:
                    self.__play_sound()
                    self.__bet(message_text)
            elif message_type == "red":
                self.total_reds += 1
                result = "red"
            elif message_type == "green":
                self.total_greens += 1
                result = "green"
        if is_valid_result:
            self.stack_type_result.append(message_type)

        return result

    def bet_after_second_red(self, message_text, message_type, has_bet=True, assertiveness=0):
        result = ""
        if assertiveness < 70.0:
            return
        last = self.stack_type_result[-1] if len(self.stack_type_result) > 0 else ""
        penultimate = (
            self.stack_type_result[-2] if len(self.stack_type_result) > 1 else ""
        )
        is_valid_result = message_type == "red" or message_type == "green"
        if last == "red" and penultimate == "red":
            if message_type == "opportunity":
                if has_bet:
                    self.__play_sound()
                    self.__bet(message_text)
            elif message_type == "red":
                self.total_reds += 1
                result = "red"
            elif message_type == "green":
                self.total_greens += 1
                result = "green"
        if is_valid_result:
            self.stack_type_result.append(message_type)

        return result

    def bet_after_third_red(self, message_text, message_type, has_bet=True):
        result = ""
        last = self.stack_type_result[-1] if len(self.stack_type_result) > 0 else ""
        penultimate = (
            self.stack_type_result[-2] if len(self.stack_type_result) > 1 else ""
        )
        third_to_last = (
            self.stack_type_result[-3] if len(self.stack_type_result) > 2 else ""
        )
        is_valid_result = message_type == "red" or message_type == "green"
        if last == "red" and penultimate == "red" and third_to_last == "red":
            if message_type == "opportunity":
                if has_bet:
                    self.__play_sound()
                    self.__bet(message_text)
            elif message_type == "red":
                self.total_reds += 1
                result = "red"
            elif message_type == "green":
                self.total_greens += 1
                result = "green"
        if is_valid_result:
            self.stack_type_result.append(message_type)

        return result
