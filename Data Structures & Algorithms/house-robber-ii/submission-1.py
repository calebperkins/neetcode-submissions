class Solution:
    def rob(self, houses: list[int]) -> int:
        # uses O(N) space
        if len(houses) < 2:
            return rob(houses)
        houses_a = houses[:-1] # exclude last house
        houses_b = houses[1:] # exclude first house
        return max(rob(houses_a), rob(houses_b))


# the recursive form
def rob_recur(houses):
    def _rob(i):
        if i >= len(houses):
            return 0
        return max(houses[i] + _rob(i+2), _rob(i+1))
    return _rob(0)


# iterative form using O(N) space
def rob_iter(houses):
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    
    # best[i] = the best value houses ends on i
    best = [0 for _ in houses]
    best[0] = houses[0]
    best[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        best[i] = max(houses[i] + best[i-2], best[i-1])
    
    return best[-1]


# iterative form using O(1) space
def rob(houses):
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    
    a = houses[0]
    b = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        c = max(houses[i] + a, b)
        a, b = b, c
    
    return b