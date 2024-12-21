"""This module includes all the custom exceptions needed for the calculator."""
UNARY_OPERATORS = ['!', '_', '~']


class EmptyExpression(Exception):
    """A custom exception, for an empty expression"""
    def __str__(self):
        return ("The expression you entered was empty.\n"
                "Please enter a non-empty mathematical expression.")


class IllegalCharacter(Exception):
    """A custom exception, for an illegal character"""
    def __init__(self, character):
        super().__init__()
        self.__character = character

    def __str__(self):
        return (f"The character '{self.__character}' can't be used in this calculator.\n"
                "Please try again without that character.")


class IllegalUseOfOperator(Exception):
    """A custom exception, for an illegal use of an operator."""
    def __init__(self, character):
        super().__init__()
        self.__character = character

    def __str__(self):
        if self.__character in UNARY_OPERATORS:
            return (f"The unary operator '{self.__character}' has to have one operand before it.\n"
                    f"Please try again according to this rule.")
        return (f"The binary operator '{self.__character}' has"
                f" to have an operand on each side of it.\n"
                f"Please try again according to this rule.")


class TooManyPointsInFloat(Exception):
    """A custom exception, for too many dots in a number."""
    def __str__(self):
        return ("You entered a decimal number with more then one decimal point.\n"
                "Please try again with a legal calculation.")


class IllegalUseOfRightUnaryOperator(Exception):
    """A custom exception, for an illegal use of a unary operator."""
    def __init__(self, operator):
        super().__init__()
        self.__operator = operator

    def __str__(self):
        return (f"The unary operator '{self.__operator}' can't be used on a negative number.\n"
                f"Please try again with a legal calculation.")


class NoParenthesisBalance(Exception):
    """A custom exception, for no balance in parentheses."""
    def __str__(self):
        return ("The amount of opening parenthesis and closing parenthesis isn't balanced.\n"
                "Please fix that and try again.")


class NoCalculation(Exception):
    """A custom exception, for an expression that include no calculation."""
    def __str__(self):
        return ("This expression includes parenthesis with no calculation inside .\n"
                "Please fix that and try again.")


class IllegalUseOfMinus(Exception):
    """A custom exception, for an illegal use of the minus operator."""
    def __str__(self):
        return ("This expression uses the minus operator in an illegal way.\n"
                "The minus operator can either be used before an operand,"
                " as an unary operator.\n"
                "Or, you can put it after another operator and"
                " then it's just part of the operand.")


class IllegalUseOfTilde(Exception):
    """A custom exception, for an illegal use of tilde."""
    def __str__(self):
        return ("This expression uses tilde illegally. "
                "You must use tilde only before an operand.\n"
                "Please try again with tilde only before an operand and not another operator.")


class IllegalUseOfFactorial(Exception):
    """A custom exception, for an illegal use of factorial."""
    def __str__(self):
        return ("This expression uses factorial on a negative or non-integer number.\n"
                "Please try again, and use factorial only on positive integers.")


class ResultIsTooLarge(Exception):
    """A custom exception, for a result too large."""
    def __str__(self):
        return ("This expression yields a number too large for this calculator.\n"
                "Please try again with smaller numbers.")


class RootOfNegative(Exception):
    """A custom exception, for a root of a negative number."""
    def __str__(self):
        return ("This expression includes a root of a negative number,"
                " which isn't legal in this calculator.\n"
                "Please try again with a legal expression.")


class NoOperationOnNumber(Exception):
    """A custom exception, for a number that isn't operated on."""
    def __str__(self):
        return ("This expression include a number that isn't operated on.\n"
                "Please try again without this problem.")


class TooLargeToSumDigits(Exception):
    """A custom exception, for number too long for '#'."""
    def __str__(self):
        return ("This expression uses the operator '#' on a number too long.\n"
                "Please try again with a shorter number.")
