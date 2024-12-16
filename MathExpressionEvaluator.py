from math import isinf

from CalculatorExceptions import NoCalculation
from Number import *


class MathExpressionEvaluator:

    @staticmethod
    def evaluate(tokens):
        numbers = []
        for token in tokens:
            if isinstance(token, Number):
                numbers.append(token)
            else:
                if token in RIGHT_UNARY_OPERATORS:
                    operand = numbers.pop()
                    result = OPERATORS[token](operand)
                    numbers.append(result)
                else:
                    try:
                        second_operand = numbers.pop()
                        first_operand = numbers.pop()
                    except Exception:
                        raise NoCalculation
                    try:
                        result = OPERATORS[token](first_operand, second_operand)
                        if isinf(result.get_value()):
                            raise Exception()
                    except Exception:
                        raise ResultIsTooLarge()
                    numbers.append(result)
        final_result = numbers[0].get_value()
        return final_result
