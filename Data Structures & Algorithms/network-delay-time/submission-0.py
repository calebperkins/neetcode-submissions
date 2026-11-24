import heapq


def network_delay(edges, n, k):
    graph = {m: [] for m in range(1, n + 1)}
    for u, v, weight in edges:
        graph[u].append((v, weight))

    distances = {}

    heap = [(0, k)]

    while heap:
        d, m = heapq.heappop(heap)

        if m in distances:
            continue

        distances[m] = d

        for x, weight in graph[m]:
            heapq.heappush(heap, (d + weight, x))

    return max(distances.values()) if len(distances) == n else -1


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        return network_delay(times, n, k)
