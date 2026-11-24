import bisect
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Node:
    time: int
    value: str


def by_time(node: Node):
    return node.time


class TimeMap:
    def __init__(self):
        self._series: dict[str, list[Node]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        series = self._series[key]
        bisect.insort(series, Node(timestamp, value), key=by_time)

    def get(self, key: str, timestamp: int) -> str:
        series = self._series[key]
        i = bisect.bisect(series, timestamp, key=by_time)
        return series[i - 1].value if i != 0 else ""
