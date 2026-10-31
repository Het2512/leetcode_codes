
from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # R[i][j]: destination after entering mirror (i,j) from left
        # D[i][j]: destination after entering mirror (i,j) from above
        R = [[-1] * n for _ in range(m)]
        D = [[-1] * n for _ in range(m)]

        # Precompute mirror destinations
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if grid[i][j] == 1:

                    # Entered mirror while moving RIGHT
                    # Reflection sends robot DOWN
                    if i + 1 < m:
                        if grid[i + 1][j] == 0:
                            R[i][j] = (i + 1) * n + j
                        else:
                            R[i][j] = D[i + 1][j]

                    # Entered mirror while moving DOWN
                    # Reflection sends robot RIGHT
                    if j + 1 < n:
                        if grid[i][j + 1] == 0:
                            D[i][j] = i * n + j + 1
                        else:
                            D[i][j] = R[i][j + 1]

        # Dynamic Programming
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):

                if dp[i][j] == 0:
                    continue

                ways = dp[i][j]

                # Move RIGHT
                if j + 1 < n:
                    if grid[i][j + 1] == 0:
                        pos = i * n + j + 1
                    else:
                        pos = R[i][j + 1]

                    if pos != -1:
                        x, y = divmod(pos, n)
                        dp[x][y] = (dp[x][y] + ways) % MOD

                # Move DOWN
                if i + 1 < m:
                    if grid[i + 1][j] == 0:
                        pos = (i + 1) * n + j
                    else:
                        pos = D[i + 1][j]

                    if pos != -1:
                        x, y = divmod(pos, n)
                        dp[x][y] = (dp[x][y] + ways) % MOD

        return dp[m - 1][n - 1]
