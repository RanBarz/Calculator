"""A module that includes class MathExpressionEvaluator,
for evaluating expression."""
from calculator_exceptions import NoCalculation, NoOperationOnNumber, ResultIsTooLarge
from number import Number, OPERATORS, RIGHT_UNARY_OPERATORS


class MathExpressionEvaluator:
    """A class that handles the evaluating of a parsed math expression."""
    @staticmethod
    def is_inf(value):
        """Checks if a number is inf."""
        return value == float('inf') or value == float('-inf')

    @staticmethod
    def evaluate(tokens):
        """evaluates a mathematical expression given in postfix notation."""
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
                        raise NoCalculation()
                    result = OPERATORS[token](first_operand, second_operand)
                    if MathExpressionEvaluator.is_inf(result.get_value()):
                        raise ResultIsTooLarge()
                    numbers.append(result)
        final_result = numbers[0].get_value()
        if len(numbers) > 1:
            raise NoOperationOnNumber()
        return final_result
