
class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7

        # Count how many numbers contain each bit
        bits = [0] * 32

        for num in nums:
            for b in range(32):
                if num & (1 << b):
                    bits[b] += 1

        ans = 0

        # Build k maximum numbers greedily
        for _ in range(k):
            num = 0

            for b in range(32):
                if bits[b] > 0:
                    num |= (1 << b)
                    bits[b] -= 1

            ans = (ans + num * num) % MOD

        return ans
