def find_min(xs: list[int]) -> int:
    # Find the first element i such that xs[i] < xs[i-1]
    lo = 0
    hi = len(xs) - 1

    # special case where we rotated 0 or N times
    if xs[lo] < xs[hi]:
        return xs[lo]

    while hi - lo > 1:
        m = (lo + hi) // 2
        # print(f"{lo}: {xs[lo]}, {hi}: {xs[hi]}")
        if xs[lo] < xs[m]:
            # rotation point must be on other side
            lo = m
        else:
            # we've flipped
            assert xs[lo] > xs[hi]
            hi = m
    # print(f"{lo}: {xs[lo]}, {hi}: {xs[hi]}")
    return xs[hi]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return find_min(nums)
