from Calculator import Calculator


class UserInterface:
    @staticmethod
    def get_expressions():
        while True:
            expression = input("Enter the calculation: ")
            result = Calculator.calculate(expression)
            print("The result is: " + str(result.get_value()))