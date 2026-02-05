
from typing import List
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:

        res = []
        idx = 0
        lenArr =len(nums)
        for num in range(len(nums)):
            res.append(0)
            if nums[num] == 0:
                idx = num
            else:
                idx = (num + nums[num]) % lenArr 
            res[num] = nums[idx]


        return res

# time complexity: O(n)
# space complexity: O(n)