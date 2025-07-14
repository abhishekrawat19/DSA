class Solution:
    def minPathSum(self, grid):
        n, m = len(grid), len(grid[0])

        # First row
        for j in range(1, m):
            grid[0][j] += grid[0][j-1]

        # First column
        for i in range(1, n):
            grid[i][0] += grid[i-1][0]

        # Rest of the grid
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[n-1][m-1]


