class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return largest_consecutive(nums)


def largest_consecutive(nums):
    seen = set(nums)
    best = 0

    # look for an n that doesn't have n+1
    for n in nums:
        if n + 1 in seen:
            continue

        # go backwards
        c = 1
        d = n
        while d - 1 in seen:
            d = d - 1
            c += 1
        best = max(best, c)
    return best
