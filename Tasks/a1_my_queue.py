"""
My little Queue
"""
from typing import Any

queue_ = []


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    queue_.append(elem)


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    return queue_.pop(0) if queue_ else None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if len(queue_) > ind:
        return queue_[ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    queue_.clear()
