from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    for i in range(0, len(container) - 1):
        for j in range(0, len(container) - i - 1):
            if container[j] > container[j + 1]:
                container[j], container[j + 1] = container[j + 1], container[j]
    return container


if __name__ == '__main__':
    container = [7, 5, -8, 0, 10, 1]
    print(sort(container))
