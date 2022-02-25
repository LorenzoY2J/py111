"""
My little Queue
"""
from typing import Any
import collections

q = collections.deque()


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    q.append(elem)


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    return q.popleft() if q else None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if len(q) > ind:
        return q[ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    q.clear()


if __name__ == '__main__':
    enqueue(1)
    enqueue(2)
    enqueue(3)
    print(q)
    dequeue()
    print(q)
