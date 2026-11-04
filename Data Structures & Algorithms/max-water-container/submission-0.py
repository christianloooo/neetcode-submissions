class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = 0
        while r > l:
            cur_height = min(heights[l], heights[r])
            cur_width = r-l
            cur_area = cur_height * cur_width
            max_area = max(max_area, cur_area)

            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return max_area


        
        