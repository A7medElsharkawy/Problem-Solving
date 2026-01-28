class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in nums :
            idx = i - 1
            if nums[idx] < 0:
                return abs(i)
            nums[idx] *= -1


"""
time complexity: O(n)
space complexity: O(1)
"""