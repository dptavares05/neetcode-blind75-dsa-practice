class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        # brute force two pointers solution
        for l in range(len(heights)): # left pointer
            for r in range(l + 1, len(heights)):# right pointer starting to the first position to the right of the left pointer
                area = (r-l) * min(heights[l], heights[r])# width is the difference of the pointers and the area is the bottleneck of the heights
                result = max(result, area) # check if new area is the biggest yet
        return result