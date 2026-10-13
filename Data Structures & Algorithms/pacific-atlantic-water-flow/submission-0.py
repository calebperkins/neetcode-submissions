def _adjacent(heights, p):
    i, j = p
    deltas = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for di, dj in deltas:
        ni = i + di
        nj = j + dj

        if 0 <= ni < len(heights) and 0 <= nj < len(heights[0]):
            yield ni, nj

def _dfs(heights, start, reachable):
    stack = [start]
    while stack:
        n = stack.pop()
        a, b = n
        if n in reachable:
            continue
        for i, j in _adjacent(heights, n):
            if heights[i][j] >= heights[a][b]:
                stack.append((i, j))
        reachable.add(n)

def pacific_atlantic(heights):
    can_reach_atlantic = set()
    can_reach_pacific = set()

    for i in range(len(heights)):
        _dfs(heights, (i, 0), can_reach_pacific)
        _dfs(heights, (i, len(heights[0]) - 1), can_reach_atlantic)
    
    for j in range(len(heights[0])):
        _dfs(heights, (0, j), can_reach_pacific)
        _dfs(heights, (len(heights)-1, j), can_reach_atlantic)

    combined = can_reach_pacific & can_reach_atlantic

    return [list(p) for p in combined]


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        return pacific_atlantic(heights)
