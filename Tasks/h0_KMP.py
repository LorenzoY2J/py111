from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    pi = [0] * len(prefix_str)
    for i in range(1, len(prefix_str)):
        j = pi[i - 1]
        while j > 0 and prefix_str[j] != prefix_str[i]:
            j = pi[j - 1]
        if prefix_str[j] == prefix_str[i]:
            j = j + 1
        pi[i] = j
    return pi


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """
    pi = _prefix_fun(substr)
    k = 0
    for i in range(len(inp_string)):
        while k > 0 and inp_string[i] != substr[k]:
            k = pi[k - 1]
        if inp_string[i] == substr[k]:
            k = k + 1
        if k == len(substr):
            return i - len(substr) + 1
