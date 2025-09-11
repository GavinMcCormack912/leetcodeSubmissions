# Last updated: 9/11/2025, 12:29:01 PM
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) == 0:
            return 0

        if len(text1) > len(text2):
            text1, text2 = text2, text1
        
        grid = [[0 for c in range(len(text2)+1)]
                for i in range(len(text1) + 1)]

        # bottom-up dp
        # check substring of text1 starting at idx 0
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    grid[i][j] = grid[i+1][j+1] + 1
                else:
                    grid[i][j] = max(grid[i+1][j], grid[i][j+1])
        return grid[0][0]
