from collections import deque
close_open = {
    ')': '(',
    ']': '[',
    '}': '{'
}


class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()
        for _ in s:
            if _ in close_open:
                if stack and stack[-1] == close_open[_]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(_)

        return False if stack else True


st = '(]'
s = Solution()
print(s.isValid(st))


# Try to avoid calling dict methods in the loop.
# Simple inversion helped me to achieve result.
