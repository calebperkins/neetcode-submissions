def can_jump(nums):
    # all numbers are non-negative. so count the consecutive zeros. if we can cross those
    # gaps we are good
    furthest_reachable = 0
    for i, v in enumerate(nums):
        # if i is greater, than we can't reach this spot and can probably return false
        if i <= furthest_reachable:
            furthest_reachable = max(furthest_reachable, v + i)
    return furthest_reachable >= len(nums) - 1

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return can_jump(nums)