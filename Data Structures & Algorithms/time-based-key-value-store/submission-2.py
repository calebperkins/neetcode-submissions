import bisect
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Node:
    time: int
    value: str


class TimeMap:
    def __init__(self):
        self._series: dict[str, list[Node]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._series:
            self._series[key] = []
        bisect.insort(self._series[key], Node(timestamp, value), key=lambda n: n.time)

    def get(self, key: str, timestamp: int) -> str:
        series = self._series[key]
        i = bisect.bisect(series, timestamp, key=lambda n: n.time)
        return series[i - 1].value if i != 0 else ""
