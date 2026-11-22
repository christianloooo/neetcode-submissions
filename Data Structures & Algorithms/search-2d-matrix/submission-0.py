class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        l, r = 0, len(matrix)-1
        while l <= r:
            mid = l + (r-l) // 2
            m = matrix[mid]
            if m[len(m)-1] < target:
                l = mid + 1
            elif m[0] > target:
                r = mid - 1
            else:
                if target in m:
                    return True
                else:
                    return False
        return False