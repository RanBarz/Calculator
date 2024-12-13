from Number import *


class TreeMathExpressionEvaluator:

    @staticmethod
    def evaluate(expression_tree):
        """
        A method that takes the abstract data type representation of the expression and evaluates it
        :return: the method will return the value.
        """
        left = expression_tree.get_left()
        right = expression_tree.get_right()
        operator = expression_tree.get_value()
        if TreeMathExpressionEvaluator.is_operator(left.get_value()):
            left.set_value(TreeMathExpressionEvaluator.evaluate(left))
        if not TreeMathExpressionEvaluator.is_right_unary(operator) and TreeMathExpressionEvaluator.is_operator(right.get_value()):
            right.set_value(TreeMathExpressionEvaluator.evaluate(right))
        left_operand = left.get_value()
        if TreeMathExpressionEvaluator.is_right_unary(operator):
            return OPERATORS[operator](left_operand)
        right_operand = right.get_value()
        return OPERATORS[operator](left_operand, right_operand)

    @staticmethod
    def is_right_unary(operator):
        return operator in RIGHT_UNARY_OPERATORS

    @staticmethod
    def is_operator(char):
        return char in OPERATORS