"""A module with the user interface class and needed constants."""
from calculator import Calculator

CALCULATOR_GUIDE = ("Calculator guide: this calculator is advanced,\n"
                    "therefore it has the regular operators and a few special ones.\n"
                    "'@' - average. example: 2@4 = 3\n"
                    "'$' - maximum. example: 2$4 = 4\n"
                    "'&' - minimum. example: 2&4 = 2\n"
                    "'~' - negate. example: 5-~3 = 8\n"
                    "'#' - sum of digits. example: 123# = 6\n")
MENU_MESSAGE = ("exit - enter 'exit' to end the program\n"
                "use - enter anything else (except ^Z or ^C) to use the calculator\n")
GET_EXPRESSION_MESSAGE = ("Enter your calculation (enter 'exit' to return to the menu, \n"
                          "enter 'help' to open the guide): ")
INVALID_INPUT_MESSAGE = "You have entered invalid input, please try again with legal input.\n"


class UserInterface:
    """The user interface class that works with the Calculator class."""
    @staticmethod
    def open_menu():
        """Opens the main menu for the calculator."""
        input_value = ""
        while input_value != "exit":
            input_value = "^Z"
            try:
                input_value = input("Welcome to the Omega Calculator.\n" + MENU_MESSAGE)
            except EOFError:
                print(INVALID_INPUT_MESSAGE)
            except KeyboardInterrupt:
                print(INVALID_INPUT_MESSAGE)
            if input_value != "^Z" and input_value != "exit":
                UserInterface.get_expressions()
                print("")

    @staticmethod
    def get_expressions():
        """Allows the user to enter mathematical expressions."""
        print("\n" + CALCULATOR_GUIDE)
        expression = ""
        while expression != "exit":
            try:
                expression = input(GET_EXPRESSION_MESSAGE)
                if expression == "help":
                    print("\n" + CALCULATOR_GUIDE)
                elif expression != "exit":
                    try:
                        result = Calculator.calculate(expression)
                        print(f"The result is: {result}\n")
                    except Exception as e:
                        print(str(e) + "\n")
            except EOFError:
                print(INVALID_INPUT_MESSAGE)
            except KeyboardInterrupt:
                print(INVALID_INPUT_MESSAGE)
