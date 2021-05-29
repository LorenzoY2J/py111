from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = (last + first) // 2
        if elem == arr[mid]:
            break
        elif elem < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1
    else:
        return None

    while mid > 0 and arr[mid - 1] == elem:
        mid -= 1
    return mid


def main():
    elem = 10
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(elem, arr))


if __name__ == '__main__':
    main()
