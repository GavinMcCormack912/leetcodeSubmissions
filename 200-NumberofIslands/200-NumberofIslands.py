# Last updated: 8/12/2025, 9:04:46 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0

        def dfs(r,c):
            if r >= rows or r < 0 or c < 0 or c >= cols or grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    dfs(r,c)
        return num_islands