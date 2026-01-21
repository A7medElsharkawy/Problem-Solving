'''
Link: https://leetcode.com/problems/top-k-frequent-elements/description/
'''

import heapq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1 # n
        
        minheap = []

        for num, f in freq.items():
            heapq.heappush(minheap, (f,num)) #log k

            if len(minheap) > k :
                heapq.heappop(minheap) #logk
         
        return [num for f, num in minheap]
    
"""
Time Complexity: O(n log k)
Space Complexity : O(k)
"""


"""
solution 2: with bucket sort
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = [[] for _ in range(len(nums) + 1)]

        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) + 1
        
        for ks,vs in dic.items():
            res[vs].append(ks)
        fres = []
        for bucket in reversed(res):
            if bucket:
                fres.extend(bucket)
                if len(fres) >= k:
                    break

        return fres

"""
Time Complexity: O(n)
Space Complexity : O(k)
"""