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
Space Complexity : O(n)
"""

