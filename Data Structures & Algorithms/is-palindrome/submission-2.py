class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = "".join(filter(str.isalnum, s))
        ss = ss.lower()
        return list(ss) == list(ss)[::-1]