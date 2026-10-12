
class Solution:
    def minSquares(self, n, m):
        count = 0

        while n > 0 and m > 0:
            if n < m:
                n, m = m, n

            count += n // m
            n = n % m

        return count
