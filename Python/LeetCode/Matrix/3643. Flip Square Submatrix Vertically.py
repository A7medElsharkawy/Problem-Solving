class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
    
        
        top = x
        bottom = x + k - 1 

        while bottom > top:
             
            for i in range(y,k+y):

                prev = grid[bottom][i]
                grid[bottom][i] = grid[top][i]
                grid[top][i] = prev
            top += 1
            bottom -= 1

        return grid
    
# Time Complexity: O(k^2) where k is the size of the submatrix being flipped.
# Space Complexity: O(1) since we are modifying the grid in place without using any