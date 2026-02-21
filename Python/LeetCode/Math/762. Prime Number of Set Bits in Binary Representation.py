class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            
            return True

        for i in range(left, right+1):
            onescount = bin(i).count('1') 
            if is_prime(onescount):
                res += 1
        return res
            