"""A module with all the testing functions needed."""
from calculator import Calculator


def evaluate(expression):
    """Simulates the advanced calculator by evaluating the expression.
    Replace this with your actual calculator function."""
    return Calculator.calculate(expression)


def test_regular_operators():
    # Basic arithmetic
    assert evaluate("2+2") == 4
    assert evaluate("10-3") == 7
    assert evaluate("4*5") == 20
    assert evaluate("8/2") == 4.0

    # Complex expressions
    assert evaluate("2+(3*4)") == 14
    assert evaluate("(10-3)/2") == 3.5
    assert evaluate("(2+3)*(5-1)") == 20


def test_average_operator():
    # Basic average
    assert evaluate("2@4") == 3
    assert evaluate("10@20") == 15

    # Nested average
    assert evaluate("(2@4)@6") == 4.5
    assert evaluate("10@(5@15)") == 10


def test_maximum_operator():
    # Basic maximum
    assert evaluate("2$4") == 4
    assert evaluate("10$3") == 10

    # Nested maximum
    assert evaluate("(2$4)$6") == 6
    assert evaluate("10$(5$15)") == 15


def test_minimum_operator():
    # Basic minimum
    assert evaluate("2&4") == 2
    assert evaluate("10&3") == 3

    # Nested minimum
    assert evaluate("(2&4)&6") == 2
    assert evaluate("10&(5&15)") == 5


def test_negate_operator():
    # Basic negate
    assert evaluate("5-~3") == 8
    assert evaluate("10+~(-2)") == 12

    # Complex negate
    assert evaluate("~(~3)") == 3
    assert evaluate("10+~(2@4)") == 7


def test_sum_of_digits_operator():
    # Basic sum of digits
    assert evaluate("123#") == 6
    assert evaluate("456#") == 15

    # Nested sum of digits
    assert evaluate("(123#)+(456#)") == 21
    assert evaluate("(12#)#") == 3  # Sum of digits of 1+2


def test_combined_operators():
    # Mixed operators with precedence consideration
    assert evaluate("(2@4)$5") == 5
    assert evaluate("(10&3)+~2") == 1
    assert evaluate("(123#)-(10$5)") == -4

    # Complex expressions
    assert evaluate("((10@20)$15)&(~(-5))") == 5
    assert evaluate("((456#)+(123#))@10") == 15.5


def test_precedence_handling():
    # Operators precedence testing
    assert evaluate("2+3*4") == 14  # '*' has higher precedence than '+'
    assert evaluate("2*(3+4)") == 14  # Parentheses alter precedence
    assert evaluate("2^3^2") == 64  # Right-associative exponentiation
    assert evaluate("10%3+2") == 3  # '%' has higher precedence than '+'
    assert evaluate("10+2@4") == 13  # '+' has lower precedence than '@'

    # Custom precedence tests
    assert evaluate("(2@4)#") == 3  # '@' before '#'
    assert evaluate("2+3*4@5") == 15.5  # '*' before '@'
    assert evaluate("(2$3)+(4&5)") == 7  # '$' and '&' have equal precedence


def test_unary_minus():
    # Unary minus basic
    assert evaluate("-1+7") == 6  # Unary minus before addition
    assert evaluate("-2^3") == -8  # Exponentiation before unary minus

    # Unary minus with parentheses
    assert evaluate("-(-3)") == 3
    assert evaluate("-(2+3)") == -5

    # Unary minus chain
    assert evaluate("-(-(-2))") == -2
    assert evaluate("-(-(-(-2)))") == 2

    # Unary minus mixed with binary minus
    assert evaluate("10--2") == 12  # First binary minus, then unary minus
    assert evaluate("10---2") == 8  # Binary minus, then unary minus twice
    assert evaluate("10----2") == 12  # Binary minus, then unary minus thrice

    # Complex cases
    assert evaluate("-2^3+5") == -3  # Unary minus with addition
    assert evaluate("10+-(2*3)") == 4  # Unary minus with multiplication
    assert evaluate("10-(-5@3)") == 14  # Unary minus with custom operators


def test_edge_cases():
    # Zero and negative numbers
    assert evaluate("0+0") == 0
    assert evaluate("0@0") == 0
    assert evaluate("-0") == 0  # Negative zero
    assert evaluate("0$(-1)") == 0  # Maximum with zero
    assert evaluate("0&(1)") == 0  # Minimum with zero

    # Complex nested precedence
    assert evaluate("-(2@4)+5$3") == 2
    assert evaluate("(2+3)*(-4)") == -20
    assert evaluate("-((2$3)@(4&1))") == -2
    assert evaluate("10-(-5)^2") == -15


def test_combined_sum_of_digits():
    # Sum of digits with other operators
    assert evaluate("123#*2") == 12
    assert evaluate("(456#)-3") == 12
    assert evaluate("(12#)*(3#)") == 9
    assert evaluate("(9#)-(3#)") == 6


def test_high_precedence_custom_operators():
    # Verify precedence of custom operators
    assert evaluate("2@4$5") == 5  # '@' has lower precedence than '$'
    assert evaluate("(5$3)&2") == 2  # Minimum after maximum
    assert evaluate("10-(2#*2)") == 6  # Sum of digits before subtraction
    assert evaluate("-2^2$4") == -16  # Exponentiation before unary minus and maximum
    assert evaluate("(3*3)#") == 9  # Sum of digits of product
