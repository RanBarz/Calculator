from CalculatorExceptions import *
from LegalTokens import LegalTokens
from Number import OPERATORS, BINARY_OPERATORS, Number, UNARY_MINUS, RIGHT_UNARY_OPERATORS
from MathExpressionParser import MathExpressionParser


class MathExpressionValidator:
    @staticmethod
    def validate(expression):
        """Uses all the validation methods on a mathematical expression."""
        methods = [method for method in dir(MathExpressionValidator)
                   if callable(getattr(MathExpressionValidator, method)) and not method.startswith("__")
                   and not method == "validate"]
        expression = MathExpressionParser.remove_white_spaces(expression)
        for method in methods:
            rule = getattr(MathExpressionValidator, method)
            rule(expression)

    @staticmethod
    def not_empty(expression):
        """Checks if the expression is empty, and if so raises a custom exception."""
        if not expression:
            raise EmptyExpression()

    @staticmethod
    def legal_tokens(expression):
        """Makes sure all the tokens in an expression are legal."""
        for token in expression:
            if (token not in [token.value for token in LegalTokens]
                    and (token not in OPERATORS or token == UNARY_MINUS)
                    and not token.isdigit()):
                raise IllegalCharacter(token)

    @staticmethod
    def use_of_operator(expression):
        """Makes sure all operators in an expression are used correctly."""
        index = 0
        tokens = MathExpressionParser.get_tokens(expression)
        MathExpressionParser.handle_unary_minus(tokens)
        MathExpressionParser.handle_minus_of_number(tokens)
        while index < len(tokens):
            token = tokens[index]
            if token in BINARY_OPERATORS:
                if index - 1 < 0 or index + 1 == len(tokens):
                    raise IllegalUseOfOperator(token)
                if ((not isinstance(tokens[index - 1], Number) and
                        tokens[index - 1] != LegalTokens.CLOSING_PARENTHESIS and
                        tokens[index - 1] not in RIGHT_UNARY_OPERATORS) or
                        (not isinstance(tokens[index + 1], Number) and
                         tokens[index + 1] != LegalTokens.OPENING_PARENTHESIS)):
                    raise IllegalUseOfOperator(token)
            elif token in RIGHT_UNARY_OPERATORS:
                if index - 1 < 0:
                    raise IllegalUseOfOperator(token)
                if (not isinstance(tokens[index - 1], Number) and
                        tokens[index - 1] != LegalTokens.CLOSING_PARENTHESIS and
                        tokens[index - 1] not in RIGHT_UNARY_OPERATORS):
                    raise IllegalUseOfOperator(token)
                elif (isinstance(tokens[index - 1], Number) and
                      Number.get_value(tokens[index - 1]) < 0):
                    raise IllegalUseOfRightUnaryOperator(token)
            index += 1

    @staticmethod
    def z_legal_numbers(expression):
        """Makes sure all numbers in an expression are legal."""
        tokens = MathExpressionParser.get_tokens(expression)
        for token in tokens:
            if isinstance(token, Number) and token.get_value() is None:
                raise TooManyPointsInFloat()

    @staticmethod
    def parenthesis_balance(expression):
        """Makes sure there is a balance between opening and closing parenthesis."""
        tokens = MathExpressionParser.get_tokens(expression)
        parenthesis_balance = 0
        for token in tokens:
            if token == LegalTokens.OPENING_PARENTHESIS:
                parenthesis_balance += 1
            elif token == LegalTokens.CLOSING_PARENTHESIS:
                parenthesis_balance -= 1
        if parenthesis_balance != 0:
            raise NoParenthesisBalance()

    @staticmethod
    def z_use_of_numbers(expression):
        """makes sure all numbers are operated on."""
        tokens = MathExpressionParser.get_tokens(expression)
        tokens = MathExpressionParser.handle_unary_minus(tokens)
        MathExpressionParser.handle_minus_of_number(tokens)
        for index in range(len(tokens)):
            if isinstance(tokens[index], Number) and index > 0:
                if tokens[index - 1] != LegalTokens.OPENING_PARENTHESIS and tokens[index - 1] not in BINARY_OPERATORS:
                    raise NoOperationOnNumber()
