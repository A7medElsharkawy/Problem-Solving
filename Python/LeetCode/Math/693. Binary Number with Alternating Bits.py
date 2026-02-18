# solution 1
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        num = n 
        while num != 0:
            t = num & 3
            print(t)
            if t == 0 or t == 3:
                return False
            num = num >> 1
        return True
#time complexity log(n)

#solution 2

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        x = n ^ (n >>1)
        return (x & x+1) == 0

# time complexity o(1)