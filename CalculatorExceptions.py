UNARY_OPERATORS = ['!', '_', '~']


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


class IllegalUseOfRightUnaryOperator(Exception):
    def __init__(self, operator):
        self.__operator = operator

    def __str__(self):
        return (f"The unary operator '{self.__operator}' can't be used on a negative number.\n"
                f"Please try again with a legal calculation.")


class NoParenthesisBalance(Exception):
    def __str__(self):
        return (f"The amount of opening parenthesis and closing parenthesis isn't balanced.\n"
                f"Please fix that and try again.")


class NoCalculation(Exception):
    def __str__(self):
        return (f"This expression includes no calculation at all, or no calculation in parenthesis.\n"
                "Please fix that and try again.")


class IllegalUseOfMinus(Exception):
    def __str__(self):
        return (f"This expression uses the minus operator in an illegal way.\n"
                f"The minus operator can either be used before a operand, as an unary operator.\n"
                f"Or, you can put it after another operator and then it's just part of the operand.")


class IllegalUseOfTilde(Exception):
    def __str__(self):
        return (f"This expression uses tilde illegally. You must use tilde only before an operand.\n"
                f"Please try again with tilde only before an operand and not another operator.")


class IllegalUseOfFactorial(Exception):
    def __str__(self):
        return (f"This expression uses factorial on a negative or non-integer number.\n"
                f"Please try again, and use factorial only on positive integers.")


class ResultIsTooLarge(Exception):
    def __str__(self):
        return ("This expression yields a number too large for this calculator.\n"
                "Please try again with smaller numbers.")


class RootOfNegative(Exception):
    def __str__(self):
        return ("This expression includes a root of a negative number, which isn't legal in this calculator.\n"
                "Please try again with a legal expression.")


class NoOperationOnNumber(Exception):
    def __str__(self):
        return ("This expression include a number that isn't operated on.\n"
                "Please try again without this problem.")
