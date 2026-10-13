def valid_tree(n: int, edges: List[List[int]]) -> bool:
    assert 0 <= len(edges) <= 5000
    assert 1 <= n <= 2000

    graph = {m: set() for m in range(n)}
    for edge in edges:
        a, b = edge
        graph[a].add(b)
        graph[b].add(a)

    seen_nodes: set[int] = set()
    stack = [(0, 0)]

    while stack:
        node, parent = stack.pop()
        if node in seen_nodes:
            return False
        seen_nodes.add(node)
        for nn in graph[node]:
            if nn != parent:
                stack.append((nn, node))

    return len(seen_nodes) == n



class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        return valid_tree(n, edges)