class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        s, j = 0 ,1
        for i in range(2,n+1):
            s, j = j, s+j
        return s
        
# Time Complexity: O(n)
# Space Complexity: O(1)