from Number import Number

OPERATORS = {"+": Number.__add__, "-": Number.__sub__, "*": Number.__mul__, "/": Number.__truediv__, "^": Number.__pow__
    , "%": Number.__mod__, "@": Number.__matmul__, "$": Number.maximum, "&": Number.__and__
    , "~": Number.__ne__, "!": Number.factorial}


class TreeMathExpressionEvaluator:

    @staticmethod
    def evaluate(expression_tree):
        """
        A method that takes the abstract data type representation of the expression and evaluates it
        :return: the method will return the value.
        """
        left = expression_tree.get_left()
        right = expression_tree.get_right()
        if TreeMathExpressionEvaluator.is_operator(left.get_value()):
            left.set_value(TreeMathExpressionEvaluator.evaluate(left))
        if TreeMathExpressionEvaluator.is_operator(right.get_value()):
            right.set_value(TreeMathExpressionEvaluator.evaluate(right))
        left_operand = left.get_value()
        right_operand = right.get_value()
        operator = expression_tree.get_value()
        return OPERATORS[operator](left_operand, right_operand)

    @staticmethod
    def is_operator(char):
        return char in OPERATORS