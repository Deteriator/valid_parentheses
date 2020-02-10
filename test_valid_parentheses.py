from valid_parentheses import *
import pytest

def test_true():
    stack = Stack()
    assert valid_parentheses("()") == True
    assert valid_parentheses("()[]{}") == True
    assert valid_parentheses("(]") == False
    assert valid_parentheses("([)]") == False
    assert valid_parentheses("{[]}") == True