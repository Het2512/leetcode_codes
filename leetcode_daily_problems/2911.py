
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # Step 1: Precompute substring costs
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                # Try every proper divisor
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Check each group
                    for r in range(d):
                        left = i + r
                        right = j - ((length - 1 - r) % d)

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        # Step 2: Dynamic Programming
        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(2 * parts, n + 1):

                for t in range(2 * (parts - 1), i - 1):

                    dp[i][parts] = min(
                        dp[i][parts],
                        dp[t][parts - 1] + cost[t][i - 1]
                    )

        return dp[n][k]
