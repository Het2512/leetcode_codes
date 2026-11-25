
class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:

        MOD = 10**9 + 7

        p = a - b

        L = d - r
        R = d - l

        n = r - l + 1

        # Sum of positions
        sum_x = (L + R) * n // 2

        # Prefix sum of ceil(y / p)
        def F(m):
            if m <= 0:
                return 0

            q = m // p
            rem = m % p

            return p * q * (q + 1) // 2 + rem * (q + 1)

        m1 = L - a
        m2 = R - a

        # Correct inclusive range
        extra = F(m2) - F(m1 - 1)

        ans = sum_x + n + 2 * b * extra

        return ans % MOD
