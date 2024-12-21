"""A module that include the Number class and its needed constants."""
from calculator_exceptions import (IllegalUseOfFactorial, ResultIsTooLarge,
                                   RootOfNegative, TooLargeToSumDigits)
from legal_tokens import LegalTokens

PRECEDENCE = {'<': 0, "+": 1, "-": 1, "*": 2, "/": 2, '_': 2.5,
              "^": 3, "%": 4, "@": 5, "$": 5, "&": 5, '!': 6, '#': 6}
UNARY_OPERATORS = ['!', '_', '~']
BINARY_OPERATORS = ["+", "-", "*", "/", "^", "%", "@", "$", "&", "_", "<"]
RIGHT_UNARY_OPERATORS = ['!', "#"]
TILDE = '~'
MINUS = '-'
UNARY_MINUS = '_'
PART_OF_NUMBER_MINUS = '<'


class Number:
    """The class that represents a number and includes all the operations for it."""
    def __init__(self, number):
        self.value = number

    def __str__(self):
        return str(self.value)

    @classmethod
    def from_string(cls, string_of_number):
        """Makes instance of Number out of a string."""
        return cls(Number.get_number(string_of_number))

    def get_value(self):
        """Returns the value of a Number"""
        return self.value

    @staticmethod
    def mul(self_number, other):
        """Returns the product of two numbers."""
        try:
            return Number(self_number.value * other.get_value())
        except Exception:
            raise ResultIsTooLarge()

    @staticmethod
    def div(self_number, other):
        """Returns the division of two numbers, raises an error if dividing by zero."""
        if other.get_value() == 0:
            raise ZeroDivisionError("This expression includes division by zero, which is illegal.\n"
                                    "Please try again with a correct expression.")
        return Number(self_number.value / other.get_value())

    @staticmethod
    def add(self_number, other):
        """Returns the sum of two numbers."""
        return Number(self_number.value + other.get_value())

    @staticmethod
    def sub(self_number, other):
        """Returns the difference between two numbers."""
        return Number(self_number.value - other.get_value())

    @staticmethod
    def power(self_number, other):
        """Returns num1 raised to the power of num2."""
        float_number = float(self_number.value)
        if other.get_value() % 1 != 0 and float_number < 0:
            raise RootOfNegative()
        try:
            return Number(pow(float_number, other.get_value()))
        except Exception:
            raise ResultIsTooLarge()

    @staticmethod
    def average(self_number, other):
        """Returns the average of two numbers."""
        return Number((self_number.value + other.get_value()) / 2)

    @staticmethod
    def maximum(self_number, other):
        """Returns the maximum of two numbers."""
        return Number(max(self_number.value, other.get_value()))

    @staticmethod
    def minimum(self_number, other):
        """Returns the minimum of two numbers."""
        return Number(min(self_number.value, other.get_value()))

    @staticmethod
    def modulo(self_number, other):
        """Returns the modulo of two numbers, raises an error if dividing by zero."""
        if other.get_value() == 0:
            raise ZeroDivisionError("Cannot perform modulo by zero.")
        return Number(self_number.value % other.get_value())

    @staticmethod
    def negate(self_number):
        """Returns the negated value of the number."""
        return Number(-self_number.value)

    @staticmethod
    def factorial_for_int(number):
        """Returns the factorial of a number, handles edge cases and uses an iterative approach."""
        if number < 0 or number % 1 != 0:
            raise IllegalUseOfFactorial()
        number = int(number)
        if number == 1 or number == 0:
            return 1
        return number * Number.factorial_for_int(number - 1)

    @staticmethod
    def factorial(self_number):
        """Tries using the factorial_for_int method."""
        try:
            return Number(Number.factorial_for_int(self_number.value))
        except Exception as e:
            if isinstance(e, IllegalUseOfFactorial):
                raise e
            raise ResultIsTooLarge()

    @staticmethod
    def count_decimal_digits(number):
        """Counts how many decimal digits a number has."""
        number_str = str(number)
        if LegalTokens.FLOATING_POINT.value in number_str:
            return len(number_str.split('.')[1])
        return 0

    @staticmethod
    def sum_digits(self_number):
        """Sums the digits of a number, including decimal numbers."""
        sum_of_digits = 0
        num = self_number.value
        num *= pow(10.0, Number.count_decimal_digits(num))
        if 'e' in str(num):
            raise TooLargeToSumDigits()
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
        if Number.is_float(string):
            return float(string)


OPERATORS = {"+": Number.add, "-": Number.sub, "*": Number.mul, "/": Number.div,
             "^": Number.power, "%": Number.modulo, "@": Number.average,
             "$": Number.maximum, "&": Number.minimum, "~": Number.negate,
             "!": Number.factorial, "_": Number.sub, "#": Number.sum_digits, "<": Number.sub}
