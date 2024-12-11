from Number import Number
from StateOfToken import StateOfToken
from LegalTokens import LegalTokens
from TreeNode import TreeNode

PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 4, "@": 5, "$": 5, "&": 5, "~": 6, "!": 6}

class TreeMathExpressionParser:

    @staticmethod
    def parse(expression):
        tokens = TreeMathExpressionParser.get_tokens(expression)
        tree = TreeMathExpressionParser.make_tree(tokens)
        return tree

    @staticmethod
    def remove_white_spaces(tokens):
        return tokens.replace(" ", "").replace("\t", "").replace("\n", "")

    @staticmethod
    def get_tokens(expression):
        expression = TreeMathExpressionParser.remove_white_spaces(expression)
        tokens = list(expression)
        tokens = TreeMathExpressionParser.handle_legal_tokens(tokens)
        tokens = TreeMathExpressionParser.handle_numbers(tokens)
        return tokens

    @staticmethod
    def handle_legal_tokens(tokens):
        for index in range(len(tokens)):
            if not tokens[index].isdigit() and not tokens[index] in PRECEDENCE:
                tokens[index] = LegalTokens(tokens[index])
        return tokens

    @staticmethod
    def handle_numbers(tokens):
        index = 0
        while index < len(tokens):
            sub_string = ""
            char = tokens[index]
            while (not char in [token for token in LegalTokens] and
                   (char.isdigit() or char == LegalTokens.FLOATING_POINT) and index < len(tokens)):
                sub_string += char
                tokens.remove(char)
                if index != len(tokens):
                    char = tokens[index]
            if sub_string:
                tokens.insert(index, Number.from_string(sub_string))
            index += 1
        return tokens

    @staticmethod
    def make_tree(tokens):
        tree = TreeNode()
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
                elif PRECEDENCE[tree.get_value()] > PRECEDENCE[token]:
                    new_tree = TreeNode(token)
                    new_tree.set_left(head)
                    tree = new_tree
                    head = tree
                else:
                    sub_tree = TreeNode(token)
                    sub_tree.set_left(tree.get_right())
                    tree.set_right(sub_tree)
                    tree = sub_tree
                state = StateOfToken.SECOND_OPERAND
        return head