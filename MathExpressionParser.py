from CalculatorExceptions import IllegalUseOfMinus, IllegalUseOfTilde, IllegalUseOfOperator
from Number import *
from LegalTokens import LegalTokens


class MathExpressionParser:

    @staticmethod
    def parse(expression):
        tokens = MathExpressionParser.get_tokens(expression)
        tokens = MathExpressionParser.handle_unary_minus(tokens)
        MathExpressionParser.handle_minus_of_number(tokens)
        postfix = MathExpressionParser.make_postfix(tokens)
        return postfix

    @staticmethod
    def get_tokens(expression):
        expression = MathExpressionParser.remove_white_spaces(expression)
        tokens = list(expression)
        tokens = MathExpressionParser.handle_legal_tokens(tokens)
        tokens = MathExpressionParser.handle_numbers(tokens)
        return tokens

    @staticmethod
    def remove_white_spaces(expression):
        return expression.replace(" ", "").replace("\t", "").replace("\n", "")

    @staticmethod
    def handle_legal_tokens(tokens):
        for index in range(len(tokens)):
            if (not tokens[index].isdigit() and not tokens[index] in PRECEDENCE
                    and not MathExpressionParser.is_tilde(tokens[index])):
                tokens[index] = LegalTokens(tokens[index])
        return tokens

    @staticmethod
    def handle_numbers(tokens):
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
        index = 1
        while index < len(tokens):
            index_to_delete = -1
            previous_token = tokens[index - 1]
            token = tokens[index]
            if MathExpressionParser.is_tilde(previous_token):
                index_to_delete = index - 1
                minus_counter = 1
            else:
                minus_counter = 0
            tilde_counter = 0
            illegal = False
            while (index < len(tokens) and (MathExpressionParser.is_tilde(token)
                   or MathExpressionParser.is_minus_part_of_number(token, previous_token))):
                if MathExpressionParser.is_tilde(token):
                    tilde_counter += 1
                minus_counter += 1
                previous_token = token
                del tokens[index]
                if index < len(tokens):
                    token = tokens[index]
                else:
                    illegal = True
            if tilde_counter > 1:
                raise IllegalUseOfTilde()
            if illegal:
                raise IllegalUseOfOperator(MINUS)
            if minus_counter % 2 != 0:
                if tokens[index] == LegalTokens.OPENING_PARENTHESIS:
                    tokens.insert(index + 1, Number(0))
                    tokens.insert(index + 2, '-')
                    tokens.insert(index+3, LegalTokens.OPENING_PARENTHESIS)
                    saved_index = index
                    parenthesis_balance = 0
                    while (parenthesis_balance != 0 or
                            tokens[index] != LegalTokens.CLOSING_PARENTHESIS):
                        if tokens == LegalTokens.OPENING_PARENTHESIS:
                            parenthesis_balance += 1
                        if tokens[index] == LegalTokens.CLOSING_PARENTHESIS:
                            parenthesis_balance -= 1
                        index += 1
                    tokens.insert(index, LegalTokens.CLOSING_PARENTHESIS)
                    index = saved_index
                else:
                    tokens[index] = OPERATORS[TILDE](tokens[index])
            if index_to_delete != -1:
                del tokens[index_to_delete]
            index += 1

    @staticmethod
    def is_minus_part_of_number(token, previous_token):
        return token == MINUS and (previous_token in PRECEDENCE or MathExpressionParser.is_tilde(previous_token))

    @staticmethod
    def is_tilde(token):
        return token == TILDE

    @staticmethod
    def handle_unary_minus(tokens):
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
        return operator in RIGHT_UNARY_OPERATORS

    @staticmethod
    def should_push(operator, operators):
        if not operators:
            return True
        if operator == LegalTokens.OPENING_PARENTHESIS or operators[-1] == LegalTokens.OPENING_PARENTHESIS:
            return True
        return PRECEDENCE[operator] > PRECEDENCE[operators[-1]]

    @staticmethod
    def make_postfix(tokens):
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