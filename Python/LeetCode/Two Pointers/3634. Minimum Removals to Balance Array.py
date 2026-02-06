from typing import List
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        
        for r in range(len(nums)):
            if nums[r] > nums[l] * k:
                l += 1
        return l


## Time complexity: O(n log n) due to sorting the array.
## Space complexity: O(nlogn) if we ignore the space used for sorting.