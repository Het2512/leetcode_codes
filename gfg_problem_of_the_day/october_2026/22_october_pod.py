class Solution:
    def minimumSum(self, s: str) -> int:
        n = len(s)

        if n == 1:
            return 0

        m = n // 2
        INF = float('inf')

        # Allowed characters for each mirrored pair
        allowed = []

        for i in range(m):
            a = s[i]
            b = s[n - 1 - i]

            # Two fixed characters must match
            if a != '?' and b != '?' and a != b:
                return -1

            if a != '?':
                allowed.append([ord(a) - ord('a')])
            elif b != '?':
                allowed.append([ord(b) - ord('a')])
            else:
                allowed.append(range(26))

        # dp[c] = minimum cost for the processed pairs,
        # ending with mirrored-pair character c.
        dp = [INF] * 26

        for c in allowed[0]:
            dp[c] = 0

        # Process remaining mirrored pairs
        for i in range(1, m):
            ndp = [INF] * 26

            # Minimum from previous character p <= c
            best = INF
            for c in range(26):
                best = min(best, dp[c] - 2 * c)
                ndp[c] = best + 2 * c

            # Minimum from previous character p >= c
            best = INF
            for c in range(25, -1, -1):
                best = min(best, dp[c] + 2 * c)
                ndp[c] = min(ndp[c], best - 2 * c)

            # Keep only characters allowed by this pair
            dp = [
                ndp[c] if c in allowed[i] else INF
                for c in range(26)
            ]

        # Even length: the middle mirrored characters
        # are adjacent and equal, so their cost is zero.
        if n % 2 == 0:
            return int(min(dp))

        # Odd length: connect the last pair to the center.
        center = s[m]

        if center != '?':
            center_allowed = [ord(center) - ord('a')]
        else:
            center_allowed = range(26)

        ans = INF

        for c in range(26):
            if dp[c] == INF:
                continue

            for z in center_allowed:
                ans = min(ans, dp[c] + 2 * abs(c - z))

        return int(ans)