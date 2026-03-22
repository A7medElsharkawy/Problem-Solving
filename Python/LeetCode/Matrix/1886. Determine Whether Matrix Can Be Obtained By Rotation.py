class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate(mat):
            new_matrix = [[0] * n for _ in range(n)]  # empty n x n matrix
            for i in range(n):
                for j in range(n):
                    new_matrix[j][n - 1 - i] = mat[i][j]  # key formula
            return new_matrix

        for _ in range(4):         # try all 4 rotations
            if mat == target:      # check equality
                return True
            mat = rotate(mat)      # rotate and try again

        return False

## Time Complexity: O(n^2) for each rotation, and we do at most 4 rotations, so O(4 * n^2) = O(n^2).
## Space Complexity: O(n^2) for the new matrix created during rotation.