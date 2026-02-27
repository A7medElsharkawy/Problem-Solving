from typing import Optional
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if root is None:
            return 0
        
        if root.val < low:
            return self.rangeSumBST(root.right,low,high)
        if root.val > high:
            return self.rangeSumBST(root.left,low,high)
        else:
            return root.val +  self.rangeSumBST(root.right,low,high) +  self.rangeSumBST(root.left,low,high)
        
#time complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree)
#space complexity: O(n) in worst case (skewed tree), O(log n