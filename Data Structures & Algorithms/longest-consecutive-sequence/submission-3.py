class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = sorted(list(set(nums)))
        max_len = 1
        counter = 1
        for i in range(1, len(l)):
            if l[i] - l[i-1] == 1:
                counter += 1
            else:
                counter = 1
            if counter > max_len:
                max_len = counter
        return max_len