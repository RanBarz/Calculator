from enum import Enum

class StateOfToken(Enum):
    OPERATOR = 1
    FIRST_OPERAND = 2
    SECOND_OPERAND = 3