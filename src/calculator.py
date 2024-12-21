"""This module has the Calculator class."""
from math_expression_validator import MathExpressionValidator
from math_expression_evaluator import MathExpressionEvaluator
from math_expression_parser import MathExpressionParser


class Calculator:
    """This class represents a calculator,
    including its only functionality: calculating an expression."""
    @staticmethod
    def calculate(expression):
        """Validates, parses, and evaluates the given mathematical expression."""
        MathExpressionValidator.validate(expression)
        parsed_expression = MathExpressionParser.parse(expression)
        result = MathExpressionEvaluator.evaluate(parsed_expression)
        return result
