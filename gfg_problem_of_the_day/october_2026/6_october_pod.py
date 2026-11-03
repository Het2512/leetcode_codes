import sys
sys.setrecursionlimit(2000000)

class Solution:
    def longIncPath(self, mat, n, m):
        
        dp = [[0] * m for _ in range(n)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            # Already calculated
            if dp[i][j] != 0:
                return dp[i][j]

            # Current cell itself
            dp[i][j] = 1

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                # Valid cell + strictly increasing
                if (0 <= ni < n and
                    0 <= nj < m and
                    mat[ni][nj] > mat[i][j]):

                    dp[i][j] = max(
                        dp[i][j],
                        1 + dfs(ni, nj)
                    )

            return dp[i][j]

        ans = 0

        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))

        return ans