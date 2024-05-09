## Code one

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int: 
        happiness.sort()
        sm = 0
        res = 0
        if k == 1:
            return happiness[-1]

        while  k != 0 and (happiness[-1]-sm) > 0  :
            res += (happiness.pop() - sm)
            sm += 1
            k -= 1         
        return res 



# code Two

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int: 
        happiness.sort()
        x = 0
        for i in range(k):
            if happiness[-1] == 0:
                break
            else:
                if i <= happiness [-1]:

                    x += (happiness.pop() - i)   

        return x        
