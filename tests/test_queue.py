import pytest
from src.queues_stacks import queue

def test_queue():
    test_queue = queue.Queue()
    test_queue.push(1)
    test_queue.push(2)
    test_queue.push(3)
    test_queue.push(4)
    test_queue.pop()
    assert test_queue.peek() == 2