def tribonacci_seq():
    a = 0
    b = 1
    c = 1

    yield a
    yield b
    yield c

    while True:
        d = a + b + c
        a, b, c = b, c, d
        yield d


def tribonacci(n: int) -> int:
    for i, t in enumerate(tribonacci_seq()):
        if i == n:
            return t


class Solution:
    def tribonacci(self, n: int) -> int:
        return tribonacci(n)
