from typing import List
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        s1 = nums[0]
        s2 = float('inf')
        s3 = float('inf')

        for i in range(1,len(nums)):
            if nums[i] < s2:
                s3 = s2
                s2 =nums[i]
            elif nums[i] < s3:
                s3 = nums[i]
        print(s1,s2,s3)
        return sum([s1,s2,s3])

# time complexity: O(n)
# space complexity: O(1)