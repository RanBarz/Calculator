from MathExpressionValidator import MathExpressionValidator
from TreeMathExpressionEvaluator import TreeMathExpressionEvaluator
from TreeMathExpressionParser import TreeMathExpressionParser


class Calculator:

    @staticmethod
    def calculate(expression):
        MathExpressionValidator.validate(expression)
        parsed_expression = TreeMathExpressionParser.parse(expression)
        result = TreeMathExpressionEvaluator.evaluate(parsed_expression)
        return result