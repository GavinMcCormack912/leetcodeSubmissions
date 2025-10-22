# Last updated: 10/22/2025, 1:22:14 PM
class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        # dp[i][j] = 0 when j <= i+1 (fewer than 3 vertices)
        for L in range(2, n):  # L = subpolygon length (in edges)
            for i in range(n - L):
                j = i + L
                dp[i][j] = float("inf")
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
        return dp[0][n - 1]