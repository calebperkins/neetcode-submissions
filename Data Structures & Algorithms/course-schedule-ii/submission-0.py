def find_ordering(num_courses, prerequisites):
    # X => Y - if you take X you can possibly take Y
    g = {n: set() for n in range(num_courses)}

    # b is required for a
    for a, b in prerequisites:
        g[b].add(a)

    indegrees = {n: 0 for n in range(num_courses)}

    for succs in g.values():
        for succ in succs:
            indegrees[succ] = indegrees.get(succ, 0) + 1

    # invariant: contains only courses with no prereqs (indegree 0)
    queue = [course for course, prereqs in indegrees.items() if prereqs == 0]
    order = []

    while queue:
        c = queue.pop()
        order.append(c)
        for succ in g[c]:
            indegrees[succ] -= 1
            if indegrees[succ] == 0:
                queue.append(succ)

    return order if len(order) == num_courses else []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return find_ordering(numCourses, prerequisites)
