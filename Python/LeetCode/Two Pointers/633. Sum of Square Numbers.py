class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        num = int(c**.5)
        l = 0

        while l <= num:
            res = l*l + num*num
            if res > c:
                num = num - 1
            elif res < c:
                l = l + 1
            else :
                return True
        return False                

        