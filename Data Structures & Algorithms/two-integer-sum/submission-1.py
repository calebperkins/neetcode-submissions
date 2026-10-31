class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return list(two_sum(nums, target))


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    # number to index
    seen = {}

    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return (seen[complement], i)
        seen[n] = i

    raise ValueError("no pair found")
