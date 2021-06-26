"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple, Dict

# import networkx as nx

root: Optional[Dict] = None


def _create_node(key, value, left=None, right=None):
    return {
        "key": key,
        "value": value,
        "left": left,
        "right": right
    }


def _find(key: int) -> Tuple[Optional[dict], Optional[dict]]:
    prev_root = None
    current_root = root
    while current_root is not None:
        if key > current_root["key"]:
            prev_root = current_root
            current_root = current_root["right"]
        elif key < current_root["key"]:
            prev_root = current_root
            current_root = current_root["left"]
        else:
            break

    return prev_root, current_root


def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    global root

    prev, current = _find(key)
    if current is not None:
        current["value"] = value
    elif prev is None:
        root = _create_node(key, value)
    else:
        if key > prev["key"]:
            prev["right"] = _create_node(key, value)
        else:
            prev["left"] = _create_node(key, value)

    # if root is None:
    #     root = _create_node(key, value)
    # return
    # current_root = root
    # while True:
    #     if key > current_root["key"]:
    #         if current_root["right"] is None:
    #             current_root["right"] = _create_node(key, value)
    #             return
    #         else:
    #             current_root = current_root["right"]
    #     elif key < current_root["key"]:
    #         if current_root["left"] is None:
    #             current_root["left"] = _create_node(key, value)
    #             return
    #         else:
    #             current_root = current_root["left"]
    #     else:
    #         current_root["value"] = value
    #         return


def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    global root

    prev, current = _find(key)

    if current is None:
        return None
    elif key > prev["key"] and prev["right"] is not None:
        if current is not None:
            current["right"] = None
    elif key < prev["key"] and prev["left"] is not None:
        if current is not None:
            current["left"] = None
    # else:
    #     current["key"] = None


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    global root

    if root is None:
        raise KeyError("Нет такого значения")

    current_node = root
    while True:
        if key == current_node["key"]:
            return current_node["key"]
        elif key > current_node["key"]:
            if current_node["right"] is None:
                raise KeyError("Нет такого значения")
            current_node = current_node["right"]
        elif key < current_node["key"]:
            if current_node["left"] is None:
                raise KeyError("Нет такого значения")
            current_node = current_node["left"]


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    global root
    root = None


def main():
    clear()
    insert(10, 10)
    print(root)
    insert(15, 15)
    print(root)
    insert(5, 5)
    print(root)
    insert(20, 20)
    print(root)
    print(find(10))
    remove(5)
    print(root)


if __name__ == '__main__':
    main()
