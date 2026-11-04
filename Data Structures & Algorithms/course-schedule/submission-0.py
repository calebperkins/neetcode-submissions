class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = build_graph(numCourses, prerequisites)
        return can_finish(graph)


def build_graph(n, prerequisites):
    # A => B, where taking A can possibly lead to B
    g = {m: [] for m in range(n)}

    # x requires y
    for x, y in prerequisites:
        g[y].append(x)

    return g


def can_finish(graph: dict[int, list[int]]) -> bool:
    indegree = {n: 0 for n in graph}
    for n, succs in graph.items():
        for m in succs:
            indegree[m] += 1

    # first take classes with indegree 0
    nodes_without_incoming = [n for n, ind in indegree.items() if not ind]

    out = []

    while nodes_without_incoming:
        n = nodes_without_incoming.pop()

        out.append(n)

        for successor in graph[n]:
            indegree[successor] -= 1

            if indegree[successor] == 0:
                nodes_without_incoming.append(successor)

    return len(out) == len(graph)
