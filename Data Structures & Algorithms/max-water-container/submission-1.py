class Solution:
    def maxArea(self, heights: List[int]) -> int:

        m = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            m = max([area, m])

            if heights[l] < heights[r]:
                templ = l
                while heights[templ] >= heights[l] and l < r:
                    l += 1
            else:
                tempr = r
                while heights[tempr] >= heights[r] and l < r:
                    r -= 1
            
        return m



        