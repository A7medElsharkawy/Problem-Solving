
from ast import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums = sorted(nums)

        i, j = 0, len(nums)-1
        res = 0
        while i < j:
            res = max(res, nums[i]+ nums[j])
            i += 1
            j -= 1
        return res
    

"""
time complexity: O(nlogn)
space complexity: O(n)
"""