from typing import List
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:

        res = 0

        for i in range(len(nums)):
            setev = set()
            setod = set()

            for j in range(i, len(nums)):

                if nums[j] % 2 == 0:
                    setev.add(nums[j])
                else:
                    setod.add(nums[j])

                if len(setev) == len(setod):
                    res = max(res, j - i + 1)
            
        return res
    
## Time complexity: O(n^2) where n is the number of elements in the nums list.
## Space complexity: O(n) in the worst case, if all elements in the nums list