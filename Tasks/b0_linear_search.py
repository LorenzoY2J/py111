"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    ind = 0
    for index, number in enumerate(arr):
        if number < arr[ind]:
            ind = index
    return ind


def main():
    arr = [1, 2, 3, -11, 1, 4, -7]
    print(min_search(arr))


if __name__ == '__main__':
    main()
