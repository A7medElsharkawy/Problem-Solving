class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        
        dp1 = 1
        dp2 = 2

        for i in range(3,n+1):
            cur = dp1 + dp2
            dp1 = dp2
            dp2 = cur
        return cur

# Time Complexity: O(n)
# Space Complexity: O(1)