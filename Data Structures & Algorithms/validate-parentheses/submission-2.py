def valid(xs):
    openers = {')': '(', '}': '{', ']': '[' }
    stack = []
    for x in xs:
        match x:
            case '(' | '{' | '[':
                stack.append(x)
            case _:
                if not stack:
                    return False
                n = stack.pop()
                if n != openers[x]:
                    return False
    return not stack

class Solution:
    def isValid(self, s: str) -> bool:
        return valid(s)