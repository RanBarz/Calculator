"""A module for an enum of non-numbers and non-operators,
 that are legal in an expression."""
from enum import Enum


class LegalTokens(Enum):
    """An enum of legal tokens."""

    FLOATING_POINT = '.'
    CLOSING_PARENTHESIS = ')'
    OPENING_PARENTHESIS = '('
