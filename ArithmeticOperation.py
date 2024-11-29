
class ArithmeticOperation:
    @staticmethod
    def multiply(num1, num2):
        """Returns the product of two numbers."""
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        """Returns the division of two numbers, raises an error if dividing by zero."""
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2

    @staticmethod
    def add(num1, num2):
        """Returns the sum of two numbers."""
        return num1 + num2

    @staticmethod
    def sub(num1, num2):
        """Returns the difference between two numbers."""
        return num1 - num2

    @staticmethod
    def power(num1, num2):
        """Returns num1 raised to the power of num2."""
        return pow(num1, num2)

    @staticmethod
    def avg(num1, num2):
        """Returns the average of two numbers."""
        return (num1 + num2) / 2

    @staticmethod
    def maximum(num1, num2):
        """Returns the maximum of two numbers."""
        return max(num1, num2)

    @staticmethod
    def minimum(num1, num2):
        """Returns the minimum of two numbers."""
        return min(num1, num2)

    @staticmethod
    def modulo(num1, num2):
        """Returns the modulo of two numbers, raises an error if dividing by zero."""
        if num2 == 0:
            raise ZeroDivisionError("Cannot perform modulo by zero.")
        return num1 % num2

    @staticmethod
    def negate(num):
        """Returns the negated value of the number."""
        return -num
    
    @staticmethod
    def factorial(num):
        """Returns the factorial of a number, handles edge cases and uses an iterative approach."""
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if num == 1 or num == 0:
            return 1
        return num * ArithmeticOperation.factorial(num - 1)