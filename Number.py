class Number:

    def __init__(self, number):
        self.__number = number

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
            raise ZeroDivisionError("Cannot divide by zero.")
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
        return Number(pow(self.__number, other.get_value()))

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
    def factorial(self):
        """Returns the factorial of a number, handles edge cases and uses an iterative approach."""
        if self.__number < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if self.__number == 1 or self.__number == 0:
            return 1
        return self.__number * Number.factorial(self.__number - 1)


    @staticmethod
    def is_number(string):
        """
        A method that determines if a string represents a number
        :param string:
        :return: True if the string can be a number, False otherwise
        """
        return string.isdigit()
    @staticmethod
    def is_integer(string):
        """
        A method that determines if a number is an integer or a float
        :param string: string representation of the number
        :return: True if the number is an integer and False otherwise
        """

    @staticmethod
    def get_integer(string):
        """ A method that get a string representation of an integer and returns its value """

    @staticmethod
    def get_float(string):
        """ A method that get a string representation of a float and returns its value """

    @staticmethod
    def get_number(string):
        """
        A method that receives a string representation of a number and returns its value
        :param string: representation of a number
        """
        return int(string)