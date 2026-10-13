# """
# Definition of Interval:
# class Interval(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
# """

# def conflicts(i1, i2):
#     return (i2.start <= i1.start < i2.end) or (i1.start <= i2.start < i1.end)

# Intervals are [start, end)
def can_attend(intervals: list[Interval]) -> bool:
    intervals = sorted(intervals, key=lambda i: i.start)

    latest = float('-inf')
    for interval in intervals:
        if interval.start < latest:
            return False
        latest = max(interval.end, latest)
    return True


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        return can_attend(intervals)