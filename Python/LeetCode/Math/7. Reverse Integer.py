class Solution:
    def reverse(self, x: int) -> int:

        num = abs(x) 
        res = 0 

        while num != 0:
            pop = num%10
            num//=10
            res = res * 10 + pop

        if x < 0:
            res = -res
        
        return res if -2**31 <= res <= 2**31 - 1 else 0

