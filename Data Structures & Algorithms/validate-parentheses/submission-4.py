class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s)%2 == 0:
            return False
        hash = {')' : '(', ']' : '[', '}' : '{'}
        stack = []
        for i in range(len(s)):
            if not stack or s[i] not in hash:
                stack.append(s[i])
            elif stack[-1] != hash[s[i]]:
                return False
            else:
                stack.pop()
        if stack:
            return False
        return True