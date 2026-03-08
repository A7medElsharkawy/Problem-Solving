class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = "".join("1" if num[i] == "0" else "0" for i, num in enumerate(nums))
        return res
# time complexity: O(N) where N is the length of the input list nums
# space complexity: O(N) where N is the length of the input list nums