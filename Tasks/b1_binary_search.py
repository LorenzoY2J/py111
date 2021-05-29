from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    low = arr[0]
    high = len(arr) - 1
    mid = len(arr) // 2
    mid_value = arr[mid]
    while mid_value != elem:
        if elem > mid_value:
            mid = mid + 1
            mid_value = (mid_value + high) // 2
        elif elem < mid_value:
            mid = mid - 1
            mid_value = (mid_value + low) // 2
        else:
            arr[mid] = mid_value
    return arr[elem]


def main():
    elem = 2
    arr = [1, 2, 3, -11, 1, 4, -7, 8]
    print(binary_search(elem, arr))


if __name__ == '__main__':
    main()

