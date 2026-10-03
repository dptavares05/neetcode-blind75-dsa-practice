class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

    ## brute force two pointers solution
        #for l in range(len(heights)): # left pointer
            #for r in range(l + 1, len(heights)):# right pointer starting to the first position to the right of the left pointer
                #area = (r-l) * min(heights[l], heights[r])# width is the difference of the pointers and the area is the bottleneck of the heights
                #result = max(result, area) # check if new area is the biggest yet
        #return result '''


        #optimal solution with two pointers moving inwards
        l, r = 0, len(heights) - 1 # initialize right and left pointer in each opposite end
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            result = max(result, area)
            if heights[l] < heights[r]:# only move the bottlenecking height
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return result