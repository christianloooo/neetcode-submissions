class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ss = "".join(filter(str.isalnum, s))
        print(list(ss)[::-1])
        return list(ss) == list(ss)[::-1]