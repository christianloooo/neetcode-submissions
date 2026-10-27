class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        mast = []
        prod = 1
        zero_count = 0
        
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                prod *= num
                
        if zero_count > 1:
            return [0] * len(nums)
            
        for num in nums:
            if zero_count == 1:
                cur = prod if num == 0 else 0
            else:
                cur = prod // num
                
            mast.append(cur)
            
        return mast
