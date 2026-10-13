# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def lca(root, p, q):
    x, y = (p, q) if p.val < q.val else (q, p)
    assert x.val < y.val

    def _lca(r):
        if x.val <= r.val <= y.val:
            return r
    
        if r.val < x.val:
            return _lca(r.right)

        return _lca(r.left)

    return _lca(root)


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return lca(root, p, q)