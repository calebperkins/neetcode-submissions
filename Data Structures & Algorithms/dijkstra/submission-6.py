import heapq

def shortest_path(n, edges, src):
    # the distance to the node from the source node. inf if unknown
    distances = {m: float('inf') for m in range(n)}
    distances[src] = 0

    # unvisited = {m for m in range(n)}

    q = [(0, src)]

    # preprocess graph
    graph = {m: {} for m in range(n)}
    for u, v, w in edges:
        if v not in graph[u] or w < graph[u][v]:
            graph[u][v] = w

    while q:
        d, u = heapq.heappop(q)
        if d > distances[u]:
            continue
        for v, u_to_v in graph[u].items():
            alt = distances[u] + u_to_v
            if alt < distances[v]:
                distances[v] = alt
                heapq.heappush(q, (alt, v))

    # transform to -1    
    return {n: d if d != float('inf') else -1 for n, d in distances.items()}


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        return shortest_path(n, edges, src)
