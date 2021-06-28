from typing import Union, Sequence
from itertools import islice

def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    prev_1, prev = stairway[0], stairway[1]
    for cost in islice(stairway, 2, len(stairway)):
        current = cost + min(prev_1, prev)
        prev_1, prev = prev, current
    return prev


if __name__ == '__main__':
    stairway = [1, 3, 5, 1]
    print(stairway_path(stairway))
