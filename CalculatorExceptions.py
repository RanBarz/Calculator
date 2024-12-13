from Number import UNARY_OPERATORS


class EmptyExpression(Exception):

    def __str__(self):
        return (f"The expression you entered was empty.\n"
                f"Please enter a non-empty mathematical expression.")

class IllegalCharacter(Exception):

    def __init__(self, character):
        self.__character = character

    def __str__(self):
        return (f"The character '{self.__character}' can't be used in this calculator.\n"
                f"Please try again without that character.")

class IllegalUseOfOperator(Exception):

    def __init__(self, character):
        self.__character = character

    def __str__(self):
        if self.__character in UNARY_OPERATORS:
            return (f"The unary operator '{self.__character}' has to have one operand before it.\n"
                    f"Please try again according to this rule.")
        return (f"The binary operator '{self.__character}' has to have an operand on each side of it.\n"
                f"Please try again according to this rule.")

class TooManyPointsInFloat(Exception):

    def __str__(self):
        return ("You entered a decimal number with more then one decimal point.\n"
                "Please try again with a legal calculation.")