from StateOfToken import StateOfToken
from TreeNode import TreeNode
from Number import Number

PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "@": 5, "$": 5, "&": 5, "~": 6, "!": 6}
OPERATORS = {"+": Number.__add__, "-": Number.__sub__, "*": Number.__mul__, "/": Number.__truediv__, "^": Number.__pow__
    , "%": Number.__mod__, "@": Number.__matmul__, "$": Number.maximum, "&": Number.__and__
    , "~": Number.__ne__, "!": Number.factorial}

class Calculator:
    def __init__(self, expression):
        self.__expression = expression

    def parse_expression(self):
        """
        A function that takes the string calculation and stores in an abstract data type,
         so it can be evaluated efficiently later.
        :return: this function will return the abstract data type representation of the string.
        """
        tokens = self.get_tokens()
        parsed_expression = Calculator.make_tree_of_tokens(tokens)
        return parsed_expression

    def validate_expression(self):
        """
        A function that makes sure the mathematical expression is legal,
        and raises the appropriate exceptions if needed
        """

    def remove_white_spaces(self):
        """
        A function that will remove all white spaces in an expression, as they are not significant
        """

    def get_tokens(self):
        lst = []
        for token in self.__expression:
            if Number.is_number(token):
                lst.append(Number.from_string(token))
            else:
                lst.append(token)
        return lst

    @staticmethod
    def make_tree_of_tokens(tokens):
        tree = TreeNode()
        head = tree
        state = StateOfToken.FIRST_OPERAND
        for token in tokens:
            if state == StateOfToken.FIRST_OPERAND:
                left = TreeNode(token)
                tree.set_left(left)
                state = StateOfToken.OPERATOR
            elif state == StateOfToken.SECOND_OPERAND:
                right = TreeNode(token)
                tree.set_right(right)
                state = StateOfToken.OPERATOR
            else:
                if tree.get_value() == 0:
                    tree.set_value(token)
                elif PRECEDENCE[tree.get_value()] >= PRECEDENCE[token]:
                    new_tree = TreeNode(token)
                    new_tree.set_left(head)
                    tree = new_tree
                    head = tree
                else:
                    sub_tree = TreeNode(token)
                    sub_tree.set_left(tree.get_right())
                    tree.set_right(sub_tree)
                    tree = sub_tree
                state = StateOfToken.SECOND_OPERAND
        return head

    @staticmethod
    def evaluate_expression(parsed_expression):
        """
        A method that takes the abstract data type representation of the expression and evaluates it
        :return: the method will return the value.
        """
        left = parsed_expression.get_left()
        right = parsed_expression.get_right()
        if Calculator.is_operator(left.get_value()):
            left.set_value(Calculator.evaluate_expression(left))
        if Calculator.is_operator(right.get_value()):
            right.set_value(Calculator.evaluate_expression(right))
        left_operand = left.get_value()
        right_operand = right.get_value()
        operator = parsed_expression.get_value()
        return OPERATORS[operator](left_operand, right_operand)

    @staticmethod
    def is_operator(char):
        return char in OPERATORS
