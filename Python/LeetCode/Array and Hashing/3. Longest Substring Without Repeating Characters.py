class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        r, l = 0,0
        longest = 0
        d = {}
        while r < len(s):
            
            if s[r] in d:
                l = max(l, d[s[r]] + 1)

            d[s[r]] = r
            longest = max(longest,r - l + 1)
            r += 1
        
        return longest


# time complexity: O(N) where N is the length of the string s
# space complexity: O(min(N,M)) where M is the size of the charset