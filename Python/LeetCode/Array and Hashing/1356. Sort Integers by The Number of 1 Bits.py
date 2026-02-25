class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        # res = []
        # for i in arr:
        #     n = 0
        #     s = i
        #     while s :
        #         n += (s & 1)
        #         s = s >> 1
        #     res.append((n, i))
        
        # res.sort()

        # return [i[1] for i in res]

        arr.sort(key= lambda num :(num.bit_count(),num))
        return arr

## time o(n log n)