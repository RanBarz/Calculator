PRECEDENCE_DICTIONARY = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "@": 5, "$": 5, "&": 5, "~": 6, "!": 6}

class Calculator:
    def __init__(self, string):
        self.__string = string

    def parse_expression(self):
        """
        A function that takes the string calculation and stores in an abstract data type,
         so it can be evaluated efficiently later.
        :return: this function will return the abstract data type representation of the string.
        """

    def validate_expression(self):
        """
        A function that makes sure the mathematical expression is legal,
        and raises the appropriate exceptions if needed
        """

    def remove_white_spaces(self):
        """
        A function that will remove all white spaces in an expression, as they are not significant
        """

    @staticmethod
    def evaluate_expression():
        """
        A method that takes the abstract data type representation of the expression and evaluates it
        :return: the method will return the value.
        """
