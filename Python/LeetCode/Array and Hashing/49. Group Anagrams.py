'''
Link : https://leetcode.com/problems/group-anagrams/description/
'''
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            group[key].append(s)

        return list(group.values())
    
'''
Time Complexity: O(m∗nlogn)
Space Complexity: O(m * n)

'''