from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        lenArr = len(heights) -1
        l, r = 0, lenArr
        while l < r:
            re = (r - l) * min(heights[l],heights[r])
            res = max(re,res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res        
    
## Time complexity: O(n) where n is the number of elements in the heights list.
## Space complexity: O(1) since we are using only a constant amount of space.