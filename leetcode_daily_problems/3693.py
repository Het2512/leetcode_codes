class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n + 1)

        for j in range(1, n + 1):
            dp[j] = float('inf')

            for i in range(max(0, j - 3), j):
                dp[j] = min(dp[j], dp[i] + costs[j - 1] + (j - i) ** 2)

        return dp[n]