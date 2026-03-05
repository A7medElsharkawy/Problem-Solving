class Solution:
    def minOperations(self, s: str) -> int:

        minzero = 0
        minone = 0

        for i in range(len(s)):

            ex_0 = '1' if i % 2 == 0 else '0'
            if s[i] != ex_0:
                minzero += 1
        
        return min(minzero, len(s) - minzero)
# time complexity: O(N) where N is the length of the string s
# space complexity: O(1)