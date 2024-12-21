from CalculatorExceptions import IllegalUseOfMinus, IllegalUseOfTilde
from Number import *
from LegalTokens import LegalTokens


class MathExpressionParser:

    @staticmethod
    def parse(expression):
        """Parses a mathematical expression to postfix notation.
           Including handling of minuses,
           and turning numbers and other tokens to representative objects."""
        tokens = MathExpressionParser.get_tokens(expression)
        tokens = MathExpressionParser.handle_unary_minus(tokens)
        MathExpressionParser.handle_minus_of_number(tokens)
        postfix = MathExpressionParser.make_postfix(tokens)
        return postfix

    @staticmethod
    def get_tokens(expression):
        """Makes tokens out of a mathematical expression.
           Including handling of numbers and parenthesis."""
        expression = MathExpressionParser.remove_white_spaces(expression)
        tokens = list(expression)
        tokens = MathExpressionParser.handle_legal_tokens(tokens)
        tokens = MathExpressionParser.handle_numbers(tokens)
        return tokens

    @staticmethod
    def remove_white_spaces(expression):
        """Removes all types of white spaces from a string."""
        return expression.replace(" ", "").replace("\t", "").replace("\n", "")

    @staticmethod
    def handle_legal_tokens(tokens):
        """Makes parenthesis and floating points into enum values.
           For better readability of the code."""
        for index in range(len(tokens)):
            if (not tokens[index].isdigit() and not tokens[index] in OPERATORS
                    and not MathExpressionParser.is_tilde(tokens[index])):
                tokens[index] = LegalTokens(tokens[index])
        return tokens

    @staticmethod
    def handle_numbers(tokens):
        """Wraps numbers in objects, for better functionality and readability."""
        index = 0
        while index < len(tokens):
            sub_string = ""
            char = tokens[index]
            while (char not in [token for token in LegalTokens if token != LegalTokens.FLOATING_POINT] and
                   (char == LegalTokens.FLOATING_POINT or char.isdigit()) and index < len(tokens)):
                if char in [token for token in LegalTokens]:
                    char = char.value
                    tokens.remove(LegalTokens.FLOATING_POINT)
                else:
                    tokens.remove(char)
                sub_string += char
                if index != len(tokens):
                    char = tokens[index]
            if sub_string:
                tokens.insert(index, Number.from_string(sub_string))
            index += 1
        return tokens

    @staticmethod
    def handle_minus_of_number(tokens):
        """Makes minuses that should be part of the operand actually part of the number object,
           and removes them from the tokens."""
        previous_token = None
        index = 0
        while index < len(tokens):
            token = tokens[index]
            minus_counter = 0
            if index > 0:
                previous_token = tokens[index - 1]
            if token == TILDE:
                minus_counter += 1
                del tokens[index]
                previous_token = TILDE
                if index < len(tokens):
                    token = tokens[index]
                else:
                    raise IllegalUseOfTilde()
            while index < len(tokens) and MathExpressionParser.is_minus_part_of_number(token, previous_token):
                minus_counter += 1
                previous_token = token
                del tokens[index]
                if index < len(tokens):
                    token = tokens[index]
                else:
                    raise IllegalUseOfMinus()
            if (minus_counter > 0 and
                    not isinstance(token, Number) and not token == LegalTokens.OPENING_PARENTHESIS):
                if previous_token == TILDE:
                    raise IllegalUseOfTilde()
                raise IllegalUseOfMinus()
            if minus_counter % 2 != 0:
                if token == LegalTokens.OPENING_PARENTHESIS:
                    tokens.insert(index + 1, Number(0))
                    tokens.insert(index + 2, PART_OF_NUMBER_MINUS)
                else:
                    tokens[index] = OPERATORS[TILDE](token)
            index += 1

    @staticmethod
    def is_minus_part_of_number(token, previous_token):
        """Checks if a minus should be part of the operand after it."""
        return token == MINUS and (previous_token in BINARY_OPERATORS or previous_token == TILDE)

    @staticmethod
    def is_tilde(token):
        """Checks if a token is tilde"""
        return token == TILDE

    @staticmethod
    def handle_unary_minus(tokens):
        """Plants zero and then a special operator that represents the unary minus where needed."""
        index = 0
        while index < len(tokens):
            count = 0
            if index == 0 or tokens[index - 1] == LegalTokens.OPENING_PARENTHESIS:
                while tokens[index] == MINUS:
                    count += 1
                    del tokens[index]
                if (count > 0 and
                        not isinstance(tokens[index], Number) and
                        not tokens[index] == LegalTokens.OPENING_PARENTHESIS):
                    raise IllegalUseOfMinus()
                if count % 2 != 0:
                    tokens.insert(index, UNARY_MINUS)
                    tokens.insert(index, Number(0))
            index += 1
        return tokens

    @staticmethod
    def is_right_unary(operator):
        """Checks if an operator is unary should be to the right of an operand."""
        return operator in RIGHT_UNARY_OPERATORS

    @staticmethod
    def should_push(operator, operators):
        """Checks if an operator should be pushed the stack of operators."""
        if not operators:
            return True
        if operator == LegalTokens.OPENING_PARENTHESIS or operators[-1] == LegalTokens.OPENING_PARENTHESIS:
            return True
        return PRECEDENCE[operator] > PRECEDENCE[operators[-1]]

    @staticmethod
    def make_postfix(tokens):
        """Takes the tokens of an infix mathematical expression,
           and return them in postfix notation."""
        postfix = []
        operators = []
        for token in tokens:
            if isinstance(token, Number):
                postfix.append(token)
            elif token == LegalTokens.OPENING_PARENTHESIS or token in OPERATORS:
                while not MathExpressionParser.should_push(token, operators):
                    postfix.append(operators.pop())
                operators.append(token)
            else:
                found_opening_parenthesis = False
                while not found_opening_parenthesis:
                    operator = operators.pop()
                    if operator == LegalTokens.OPENING_PARENTHESIS:
                        found_opening_parenthesis = True
                    else:
                        postfix.append(operator)
        while operators:
            postfix.append(operators.pop())
        return postfix
