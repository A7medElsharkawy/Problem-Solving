class Solution:
    def minimumDeletions(self, s: str) -> int:
        countB= 0
        deletion = 0
        for i in s:
            if i == "b":
                countB += 1
            else:
                deletion = min(deletion + 1, countB)
        return deletion

## Time complexity: O(n) where n is the length of the string.
## Space complexity: O(1) since we are using only a constant amount of space.