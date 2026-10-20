class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i
        for i in range(len(nums)):
            dummy = target - nums[i]
            if dummy in hash and i != hash[dummy]:
                return [i, hash[dummy]]