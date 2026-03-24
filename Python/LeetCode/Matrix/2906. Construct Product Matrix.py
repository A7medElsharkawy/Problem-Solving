class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        pfix = 1
        sufix = 1
        res = [[1]* len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res[i][j] = pfix
                pfix = (pfix *grid[i][j]) %12345
        
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                res[i][j]  = (res[i][j] * sufix) %12345
                sufix = (sufix* grid[i][j]) %12345
        return res
        
## Time complexity: O(m*n) where m is the number of rows and n is the number of columns in the grid.
## Space complexity: O(m*n) for the result matrix.