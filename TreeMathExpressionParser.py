from CalculatorExceptions import IllegalUseOfMinus, IllegalUseOfTilde
from Number import *
from StateOfToken import StateOfToken
from LegalTokens import LegalTokens
from TreeNode import TreeNode


class TreeMathExpressionParser:

    @staticmethod
    def parse(expression):
        tokens = TreeMathExpressionParser.get_tokens(expression)
        tokens = TreeMathExpressionParser.handle_unary_minus(tokens)
        TreeMathExpressionParser.handle_minus_of_number(tokens)
        tree = TreeMathExpressionParser.make_tree(tokens)
        return tree

    @staticmethod
    def get_tokens(expression):
        expression = TreeMathExpressionParser.remove_white_spaces(expression)
        tokens = list(expression)
        tokens = TreeMathExpressionParser.handle_legal_tokens(tokens)
        tokens = TreeMathExpressionParser.handle_numbers(tokens)
        return tokens

    @staticmethod
    def remove_white_spaces(expression):
        return expression.replace(" ", "").replace("\t", "").replace("\n", "")

    @staticmethod
    def handle_legal_tokens(tokens):
        for index in range(len(tokens)):
            if (not tokens[index].isdigit() and not tokens[index] in PRECEDENCE
                    and not TreeMathExpressionParser.is_tilde(tokens[index])):
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
            if TreeMathExpressionParser.is_tilde(previous_token):
                index_to_delete = index - 1
                minus_counter = 1
            else:
                minus_counter = 0
            tilde_counter = 0
            while (TreeMathExpressionParser.is_tilde(token)
                   or TreeMathExpressionParser.is_minus_part_of_number(token, previous_token)):
                if TreeMathExpressionParser.is_tilde(token):
                    tilde_counter += 1
                minus_counter += 1
                previous_token = token
                del tokens[index]
                token = tokens[index]
            if tilde_counter > 1:
                raise IllegalUseOfTilde()
            if minus_counter % 2 != 0:
                if tokens[index] in LegalTokens:
                    tokens.insert(index + 1, Number(0))
                    tokens.insert(index + 2, '-')
                else:
                    tokens[index] = OPERATORS[TILDE](tokens[index])
            if index_to_delete != -1:
                del tokens[index_to_delete]
            index += 1

    @staticmethod
    def is_minus_part_of_number(token, previous_token):
        return token == MINUS and (previous_token in PRECEDENCE or TreeMathExpressionParser.is_tilde(previous_token))

    @staticmethod
    def is_tilde(token):
        return token == TILDE

    @staticmethod
    def handle_unary_minus(tokens):
        index = 0
        count = 0
        while index < len(tokens):
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
    def make_tree(tokens):
        tree = TreeNode()
        tree_father = None
        head = tree
        state = StateOfToken.FIRST_OPERAND
        after_parenthesis = False
        parenthesis_balance = 0
        for token in tokens:
            if after_parenthesis:
                if token == LegalTokens.OPENING_PARENTHESIS:
                    parenthesis_balance += 1
                elif token == LegalTokens.CLOSING_PARENTHESIS:
                    parenthesis_balance -= 1
                if parenthesis_balance == 0:
                    after_parenthesis = False
            elif state == StateOfToken.FIRST_OPERAND:
                if token == LegalTokens.OPENING_PARENTHESIS:
                    parenthesis_balance = 1
                    index = tokens.index(LegalTokens.OPENING_PARENTHESIS)
                    left = TreeMathExpressionParser.make_tree(tokens[index + 1:])
                    after_parenthesis = True
                else:
                    left = TreeNode(token)
                tree.set_left(left)
                state = StateOfToken.OPERATOR
            elif state == StateOfToken.SECOND_OPERAND:
                if token == LegalTokens.OPENING_PARENTHESIS:
                    parenthesis_balance = 1
                    index = tokens.index(LegalTokens.OPENING_PARENTHESIS)
                    right = TreeMathExpressionParser.make_tree(tokens[index + 1:])
                    after_parenthesis = True
                else:
                    right = TreeNode(token)
                tree.set_right(right)
                state = StateOfToken.OPERATOR
            else:
                if token == LegalTokens.CLOSING_PARENTHESIS:
                    return head
                if tree.get_value() is None:
                    tree.set_value(token)
                elif (not TreeMathExpressionParser.is_right_unary(token) and
                      PRECEDENCE[tree.get_value()] > PRECEDENCE[token]):
                    new_tree = TreeNode(token)
                    new_tree.set_left(tree)
                    tree = new_tree
                    if tree_father is None:
                        head = tree
                    else:
                        tree_father.set_right(tree)
                else:
                    sub_tree = TreeNode(token)
                    sub_tree.set_left(tree.get_right())
                    tree.set_right(sub_tree)
                    if not TreeMathExpressionParser.is_right_unary(token):
                        tree_father = tree
                        tree = sub_tree
                if TreeMathExpressionParser.is_right_unary(token):
                    state = StateOfToken.OPERATOR
                else:
                    state = StateOfToken.SECOND_OPERAND
        return head
