"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


def copy(head: Node) -> Node:
    # 1. make copies of all the objects
    copies: dict[Node, Node] = {}  # old to new

    h = head
    while h:
        copies[h] = Node(h.val)
        h = h.next

    # 2. link everything up
    h = head
    while h:
        copy = copies[h]
        copy.next = copies[h.next] if h.next else None
        copy.random = copies[h.random] if h.random else None
        h = h.next

    return copies[head]


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        return copy(head) if head else None
