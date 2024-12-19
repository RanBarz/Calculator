from MathExpressionValidator import MathExpressionValidator
from MathExpressionEvaluator import MathExpressionEvaluator
from MathExpressionParser import MathExpressionParser


class Calculator:

    @staticmethod
    def calculate(expression):
        """Validates, parses, and evaluates the given mathematical expression."""
        MathExpressionValidator.validate(expression)
        parsed_expression = MathExpressionParser.parse(expression)
        result = MathExpressionEvaluator.evaluate(parsed_expression)
        return result
