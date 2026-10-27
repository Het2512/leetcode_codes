
class Solution:
    def getMaxWeight(self, s):
        n = len(s)

        # dp[i] = maximum weight for the first i characters
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Option 1: Leave current character unpaired
            dp[i] = dp[i - 1] + 1

            # Option 2: Pair current character with previous character
            if i >= 2:
                cost = 0 if s[i - 2] != s[i - 1] else 1
                dp[i] = max(dp[i], dp[i - 2] + 4 - cost)

        return dp[n]
