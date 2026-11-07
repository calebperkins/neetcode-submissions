"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


def clone(node: Node | None) -> Node | None:
    if node is None:
        return None

    seen = set()
    stack = [node]

    while stack:
        n = stack.pop()

        if n in seen:
            continue
        seen.add(n)

        stack.extend(n.neighbors)

    by_id = {id(n): n for n in seen}
    new_nodes = {orig_id: Node(n.val) for orig_id, n in by_id.items()}

    for orig_id, orig_node in by_id.items():
        new_node = new_nodes[orig_id]
        new_neighbors = [new_nodes[id(n)] for n in orig_node.neighbors]
        new_node.neighbors = new_neighbors

    return new_nodes[id(node)]


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        return clone(node)
