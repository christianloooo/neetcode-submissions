class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(set(nums))
        return sorted(nums) != sorted(list(set(nums)))