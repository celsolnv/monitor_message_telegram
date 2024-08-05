
# Adicionar tipo para o resultado da aposta
#  Vai ser red ou green
from typing import Literal 

TResult = Literal["red", "green"]

class Wallet:
    def __init__(self) -> None:
        self.balance = 0
        self.bets = 0
        self.wins = 0
        self.losses = 0
        self.base_value = 10
    
    def set_base_value(self, base_value):
        self.base_value = base_value
    def set_balance(self, balance):
        self.balance = balance 
        
    def four_x(self, indice_bet, current_result: TResult, last_result: TResult):
        # Na primeira aposta, o valor base é 2x
        value = self.base_value
        if (indice_bet == 1):
            value = value
        elif (indice_bet == 2):
            if (last_result == 'green'):
                value = value * 2
            elif (last_result == 'red'):
                value = value
        elif (indice_bet == 3):
            if (last_result == 'green' ):
                value = value * 2
            elif (last_result == 'red'):
                value = value

        