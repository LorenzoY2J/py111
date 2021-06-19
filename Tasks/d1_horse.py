from typing import List


def pprint(field: List[List[int]]):
    for i in range(len(field) - 1, -1, -1):
        s = "|".join(f"{field[i][j]: ^5}" for j in range(len(field[i])))
        print(s)


_possible_steps = ((-1, 2), (2, -1), (1, 2), (2, 1))


def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    field = [[0] * shape[1] for _ in range(shape[0])]
    field[0][0] = 1
    for i in range(shape[0]):
        for j in range(shape[1]):
            if field[i][j] != 0:
                for step in _possible_steps:
                    new_i = step[0] + i
                    new_j = step[1] + j
                    if 0 <= new_i < shape[0] and 0 <= new_j < shape[1]:
                        field[new_i][new_j] += field[i][j] * 2
    pprint(field)


def main():
    calculate_paths((8, 8), (7, 7))


if __name__ == '__main__':
    main()
