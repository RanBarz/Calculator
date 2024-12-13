from CalculatorExceptions import *
from LegalTokens import LegalTokens
from Number import OPERATORS, BINARY_OPERATORS, Number, UNARY_MINUS, RIGHT_UNARY_OPERATORS
from TreeMathExpressionParser import TreeMathExpressionParser

class MathExpressionValidator:
    @staticmethod
    def validate(expression):
        methods = [method for method in dir(MathExpressionValidator)
                   if callable(getattr(MathExpressionValidator, method)) and not method.startswith("__")
                   and not method == "validate"]
        for method in methods:
            rule = getattr(MathExpressionValidator, method)
            rule(expression)

    @staticmethod
    def not_empty(expression):
        expression = TreeMathExpressionParser.remove_white_spaces(expression)
        if not expression:
            raise EmptyExpression()

    @staticmethod
    def legal_tokens(expression):
        for token in expression:
            if (not token in [token.value for token in LegalTokens]
                    and (not token in OPERATORS or token == UNARY_MINUS)
                    and not token.isdigit()):
                raise IllegalCharacter(token)

    @staticmethod
    def use_of_operator(expression):
        index = 0
        tokens = TreeMathExpressionParser.get_tokens(expression)
        TreeMathExpressionParser.handle_minus_of_number(tokens)
        while index < len(tokens):
            token = tokens[index]
            if token in BINARY_OPERATORS:
                if index - 1 < 0 or index + 1 == len(tokens):
                    raise IllegalUseOfOperator(token)
                if ((not isinstance(tokens[index - 1], Number) and
                     tokens[index - 1] != LegalTokens.CLOSING_PARENTHESIS)
                        or (not isinstance(tokens[index + 1], Number) and
                            tokens[index + 1] != LegalTokens.OPENING_PARENTHESIS)):
                    raise IllegalUseOfOperator(token)
            elif token in RIGHT_UNARY_OPERATORS:
                if index - 1 < 0:
                    raise IllegalUseOfOperator(token)
                if (not isinstance(tokens[index - 1], Number) and
                     tokens[index - 1] != LegalTokens.CLOSING_PARENTHESIS):
                    raise IllegalUseOfOperator(token)
            index += 1