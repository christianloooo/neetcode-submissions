class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            if num in hash:
                hash[num] = hash[num] + 1
            else:
                hash[num] = 1
        e = []
        for i in range(k):
            max_key = max(hash, key=hash.get)
            e.append(max_key)
            hash.pop(max_key)
        return e
        