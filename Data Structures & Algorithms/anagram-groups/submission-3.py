class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for str in strs:
            s = ''.join(sorted(str))
            hash[s].append(str)
        return list(hash.values())