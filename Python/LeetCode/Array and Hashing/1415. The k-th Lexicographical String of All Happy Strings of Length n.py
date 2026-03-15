class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        #sol 1

        chars = ['a','b','c']
        result = []
        def backtrack(path):
            if len(path)== n:
                result.append(path)
                return
            
            for i in chars:
                if len(path) ==0 or path[-1] != i:
                    backtrack(path+i)
        backtrack("")
        return result[k-1] if len(result) >= k else ""
        ## sol 2

        total_happy = 3 *(2**(n-1))

        res = []
        choices = 'abc'
        l, r = 1, total_happy #1 12

        for i in range(n):
            cur = l # 1
            part_size = (r - l + 1) // len(choices)

            for c in choices:
                if k in range(cur, cur + part_size):
                    res.append(c)
                    l = cur
                    r = cur + part_size - 1
                    choices = "abc".replace(c,"")
                    break
                cur += part_size
        return "".join(res)
