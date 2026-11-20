class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        window = set()
        r = 0
        ss = list(s)
        for i in range(len(ss)):
            while ss[i] in window:
                window.remove(s[r])
                r+=1
            window.add(ss[i])
            counter = len(window)
            if max < counter: max=counter
        return max