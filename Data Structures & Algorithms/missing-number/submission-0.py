class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        current_sum = sum(nums)
        expected = (n * (n + 1)) // 2
        return abs(current_sum - expected)

