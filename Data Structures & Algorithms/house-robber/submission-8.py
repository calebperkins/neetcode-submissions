class Solution:
    def rob(self, houses: list[int]) -> int:
        return rob(houses)

# the recursive form
# def rob(houses):
#     def _rob(i):
#         if i >= len(houses):
#             return 0
#         return max(houses[i] + _rob(i+2), _rob(i+1))
#     return _rob(0)


def rob(houses):
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