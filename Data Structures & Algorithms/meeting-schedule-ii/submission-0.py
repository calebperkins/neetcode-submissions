"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        return min_meeting_rooms(intervals)


def min_meeting_rooms(intervals) -> int:
    intervals = sorted(intervals, key=lambda i: i.start)

    # A heap of the next room opening up
    rooms_by_next_available: list[int] = []

    for i in intervals:
        if not rooms_by_next_available:
            rooms_by_next_available.append(i.end)
            continue

        first_available = rooms_by_next_available[0]

        if first_available <= i.start:
            # this room works
            heapq.heapreplace(rooms_by_next_available, i.end)
        else:
            # need a new room
            heapq.heappush(rooms_by_next_available, i.end)

    return len(rooms_by_next_available)
