class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        target = sorted(s1)
        top = len(s1)
        window = list(s2)[:top]
        if sorted(window) == target:
            return True
        for i in range(top, len(s2)):
            window.pop(0)
            window.append(s2[i])
            if sorted(window) == target:
                return True
        return sorted(window) == target