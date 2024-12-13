from Calculator import Calculator

CALCULATOR_GUIDE = ("Calculator guide: this calculator is advanced,\n"
              "therefore it has the regular operators and a few special ones.\n"
              "'@' - average. example: 2@4 = 3\n"
              "'$' - maximum. example: 2$4 = 4\n"
              "'&' - minimum. example: 2&4 = 2\n"
              "'~' - negate. example: 5-~3 = 8\n"
              "'#' - sum of digits. example: 123# = 6\n")
MENU_MESSAGE= ("exit - enter 'exit' to end the program\n"
              "use - enter 'use' to use the calculator\n")
GET_EXPRESSION_MESSAGE = "Enter your calculation (enter 'exit' to return to the menu): "

class UserInterface:

    @staticmethod
    def open_menu():
        input_value = input("Welcome to the Omega Calculator.\n" + MENU_MESSAGE)
        while input_value != "exit":
            UserInterface.get_expressions()
            print("")
            input_value = input(MENU_MESSAGE)

    @staticmethod
    def get_expressions():
        print("\n" + CALCULATOR_GUIDE)
        expression = input(GET_EXPRESSION_MESSAGE)
        while expression != "exit":
            try:
                result = Calculator.calculate(expression)
                print(f"The result is: {result}\n")
            except Exception as e:
                print(e)
            expression = input(GET_EXPRESSION_MESSAGE)