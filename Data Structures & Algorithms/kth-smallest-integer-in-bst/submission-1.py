# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def inorder_traversal(root: TreeNode):
    parents = []

    def go_left(node):
        while node:
            parents.append(node)
            node = node.left

    go_left(root)
    while parents:
        n = parents.pop()
        yield n
        if n.right:
            go_left(n.right)


# O(k), reads only k nodes
def smallest(root: TreeNode, k: int):
    assert k >= 1
    count = 0
    for node in inorder_traversal(root):
        count += 1
        if count == k:
            return node.val


# This reads the full tree, not taking advantage of the BST structure.
# This is O(N log(k))
def smallest_slow(root: TreeNode, k: int):
    import heapq

    assert k >= 1

    def node_iterator():
        stack = [root]
        while stack:
            n = stack.pop()
            yield n
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)

    k_smallest = heapq.nsmallest(k, node_iterator(), key=lambda n: n.val)
    return k_smallest[-1].val


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return smallest(root, k)
