import heapq
from collections import Counter

TODO = 1

def min_window(haystack: str, needles: str) -> str | None:
    # Map each needle to its positions in the haystack, e.g.
    # X: 6
    # Y: 5
    # Z: 2, 8
    locations: dict[str, list[int]] = {n: [] for n in needles}
    for i, char in enumerate(haystack):
        if char in locations:
            locations[char].append(i)
    
    # how much we need of of each needle
    need: dict[str, int] = Counter(needles)

    if any(len(locations[n]) < c for n, c in need.items()):
        return # not enough copies of some needle

    # heap of (position, needle, index into that needle's position list)
    heap: list[tuple[int, str, int]] = [(lst[0], n, 0) for n, lst in locations.items()]
    heapq.heapify(heap)

    # location of furthest right unique needle (e.g. X: 6)
    hi = max(locations[n][c - 1] for n, c in need.items())   # last element of each block
    # the smallest window containing all needles so far, e.g. (2, 6)
    best: tuple[int, int] = (heap[0][0], hi)
    assert best[1] >= best[0]


    # try shifting the window to the right. we get the next left position from the heap
    while True:
        lo, needle, k = heapq.heappop(heap)
        if hi - lo < best[1] - best[0]:
            best = (lo, hi) # record this candidate
        required = need[needle]
        if k == len(locations[needle]) - required:
            break  # can't move the left edge past the last occurrence of needle
        hi = max(hi, locations[needle][k + required])
        heapq.heappush(heap, (locations[needle][k + 1], needle, k + 1)) 

    assert best[1] >= best[0]
    return haystack[best[0]:best[1] + 1]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return min_window(s, t) or ""