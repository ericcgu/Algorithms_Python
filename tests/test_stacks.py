import pytest
from src.queues_stacks import stacks

def test_stack():
    test_stack = stacks.Stack()
    test_stack.push(1)
    test_stack.push(2)
    test_stack.push(3)
    test_stack.push(4)
    test_stack.pop()
    assert test_stack.peek() == 3