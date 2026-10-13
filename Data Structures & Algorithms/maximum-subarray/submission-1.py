# too slow... recursive without memoization
def max_subarray_recursive(nums):
    assert nums, "expected non-empty array"
    
    def find_max(i):
        if i == 0:
            return nums[0]
        # Either extend the previous subarray or start a new one
        return max(nums[i], nums[i] + find_max(i - 1))

    return max(find_max(i) for i in range(len(nums)))


def max_subarray(nums):
    best_ending_here = nums[0]
    best_overall = best_ending_here

    for i in range(1, len(nums)):
        # Either extend the previous subarray or start a new one
        best_ending_here = max(nums[i], nums[i] + best_ending_here)
        best_overall = max(best_overall, best_ending_here)
    return best_overall

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return max_subarray(nums)