from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        lenArr = len(nums)      
        i , j = 0, k - 1
        res = float('inf')
        while j < lenArr:
            res = min(res,nums[j] - nums[i])
            i += 1
            j += 1
        return res


"""
time complexity: O(NlogN) where N is the length of nums
space complexity: O(1)
"""