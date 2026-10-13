def climb_stairs(n):
    # if n == 0:
    #     return 1
    # if n == 1:
    #     return 1
    # return climb_stairs(n-1) + climb_stairs(n-2)
    x = 0
    y = 1
    for _ in range(n):
        x, y = y, x + y
    return y


class Solution:
    def climbStairs(self, n: int) -> int:
        return climb_stairs(n)