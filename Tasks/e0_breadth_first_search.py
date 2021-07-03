from typing import Hashable, List
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    already_seen = {start_node}
    queue = [start_node]
    sorted_node = []

    while queue:
        node = queue.pop(0)
        sorted_node.append(node)

        for neighbor in g.neighbors(node):
            if neighbor not in already_seen:
                already_seen.add(neighbor)
                queue.append(neighbor)

    return sorted_node


bfs()