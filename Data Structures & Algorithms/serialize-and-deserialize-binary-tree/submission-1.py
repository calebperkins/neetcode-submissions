# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def serialize(root):
    tokens = []
    stack = deque([root])
    while stack:
        n = stack.pop()
        if n:
            tokens.append(str(n.val))
            stack.append(n.right)
            stack.append(n.left)
        else:
            tokens.append("N")
    return ",".join(tokens)


def deserialize(data):
    raw_tokens = data.split(",")
    tokens = [None if t == "N" else TreeNode(int(t)) for t in raw_tokens]

    # return the root and the _inclusive_ ending index
    def build(start: int) -> tuple[TreeNode | None, int]:
        t = tokens[start]
        if t is None:
            return (t, start)
        lft, end_of_lft = build(start + 1)
        rgt, end_of_rgt = build(end_of_lft + 1)
        t.left = lft
        t.right = rgt
        return t, end_of_rgt

    root, _ = build(0)
    return root


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: TreeNode | None) -> str:
        return serialize(root)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode | None:
        return deserialize(data)
