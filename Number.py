from CalculatorExceptions import IllegalUseOfFactorial, ResultIsTooLarge, RootOfNegative
from LegalTokens import LegalTokens

PRECEDENCE = {'<': 0, "+": 1, "-": 1, "*": 2, "/": 2, '_': 2.5, "^": 3, "%": 4, "@": 5, "$": 5, "&": 5, '!': 6, '#': 6}
UNARY_OPERATORS = ['!', '_', '~']
BINARY_OPERATORS = ["+", "-", "*", "/", "^", "%", "@", "$", "&", "_", "<"]
RIGHT_UNARY_OPERATORS = ['!', "#"]
TILDE = '~'
MINUS = '-'
UNARY_MINUS = '_'
PART_OF_NUMBER_MINUS = '<'


class Number:

    def __init__(self, number):
        self.__number = number

    def __str__(self):
        return str(self.__number)

    @classmethod
    def from_string(cls, string_of_number):
        return cls(Number.get_number(string_of_number))

    def get_value(self):
        return self.__number

    @staticmethod
    def __mul__(self, other):
        """Returns the product of two numbers."""
        return Number(self.__number * other.get_value())

    @staticmethod
    def __truediv__(self, other):
        """Returns the division of two numbers, raises an error if dividing by zero."""
        if other.get_value() == 0:
            raise ZeroDivisionError("This expression includes division by zero, which is illegal.\n"
                                    "Please try again with a correct expression.")
        return Number(self.__number / other.get_value())

    @staticmethod
    def __add__(self, other):
        """Returns the sum of two numbers."""
        return Number(self.__number + other.get_value())

    @staticmethod
    def __sub__(self, other):
        """Returns the difference between two numbers."""
        return Number(self.__number - other.get_value())

    @staticmethod
    def __pow__(self, other):
        """Returns num1 raised to the power of num2."""
        float_number = float(self.__number)
        if other.get_value() % 1 != 0 and float_number < 0:
            raise RootOfNegative()
        return Number(pow(float_number, other.get_value()))

    @staticmethod
    def __matmul__(self, other):
        """Returns the average of two numbers."""
        return Number((self.__number + other.get_value()) / 2)

    @staticmethod
    def maximum(self, other):
        """Returns the maximum of two numbers."""
        return Number(max(self.__number, other.get_value()))

    @staticmethod
    def __and__(self, other):
        """Returns the minimum of two numbers."""
        return Number(min(self.__number, other.get_value()))

    @staticmethod
    def __mod__(self, other):
        """Returns the modulo of two numbers, raises an error if dividing by zero."""
        if other.get_value() == 0:
            raise ZeroDivisionError("Cannot perform modulo by zero.")
        return Number(self.__number % other.get_value())

    @staticmethod
    def __invert__(self):
        """Returns the negated value of the number."""
        return Number(-self.__number)

    @staticmethod
    def factorial_for_int(number):
        """Returns the factorial of a number, handles edge cases and uses an iterative approach."""
        if number < 0:
            raise IllegalUseOfFactorial()
        if number == 1 or number == 0:
            return 1
        return number * Number.factorial_for_int(number - 1)

    @staticmethod
    def factorial(self):
        try:
            return Number(Number.factorial_for_int(self.__number))
        except Exception:
            raise ResultIsTooLarge()

    @staticmethod
    def count_decimal_digits(number):
        number_str = str(number)
        if LegalTokens.FLOATING_POINT.value in number_str:
            return len(number_str.split('.')[1])
        return 0

    @staticmethod
    def sum_digits(self):
        sum_of_digits = 0
        num = self.__number
        num *= pow(10, Number.count_decimal_digits(num))
        while num != 0:
            sum_of_digits += num % 10
            num //= 10
        return Number(sum_of_digits)

    @staticmethod
    def is_number(string):
        """
        A method that determines if a string represents a number
        :param string:
        :return: True if the string can be a number, False otherwise
        """
        return string.isdigit() or Number.is_float(string)

    @staticmethod
    def is_integer(string):
        """
        A method that determines if a number is an integer
        :param string: string representation of the number
        :return: True if the number is an integer and False otherwise
        """
        return string.isdigit()

    @staticmethod
    def is_float(string):
        """
        A method that determines if a number is a float
        :param string: string representation of the number
        :return: True if the number is a float and False otherwise
        """
        try:
            float(string)
            return True
        except ValueError:
            return False

    @staticmethod
    def get_number(string):
        """
        A method that receives a string representation of a number and returns its value
        :param string: representation of a number
        """
        if Number.is_integer(string):
            return int(string)
        elif Number.is_float(string):
            return float(string)


OPERATORS = {"+": Number.__add__, "-": Number.__sub__, "*": Number.__mul__, "/": Number.__truediv__,
             "^": Number.__pow__, "%": Number.__mod__, "@": Number.__matmul__, "$": Number.maximum, "&": Number.__and__,
             "~": Number.__invert__, "!": Number.factorial, "_": Number.__sub__, "#": Number.sum_digits,
             "<": Number.__sub__}
