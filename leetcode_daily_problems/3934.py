
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:

        n = len(nums)

        MOD1 = 1000000007
        MOD2 = 1000000009
        BASE = 911382323

        def check(length):

            seen = set()
            duplicate = set()

            h1 = h2 = 0

            p1 = pow(BASE, length, MOD1)
            p2 = pow(BASE, length, MOD2)

            for i in range(n):

                h1 = (h1 * BASE + nums[i]) % MOD1
                h2 = (h2 * BASE + nums[i]) % MOD2

                if i >= length:
                    h1 = (h1 - nums[i - length] * p1) % MOD1
                    h2 = (h2 - nums[i - length] * p2) % MOD2

                if i >= length - 1:

                    key = h1 * MOD2 + h2

                    if key in seen:
                        duplicate.add(key)
                    else:
                        seen.add(key)

            return len(seen) > len(duplicate)

        left, right = 1, n

        while left < right:

            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
