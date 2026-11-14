
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        ans = float('inf')
        n = len(nums)

        for i in range(n):
            total = 0

            for j in range(i, n):
                total += nums[j]

                length = j - i + 1

                if l <= length <= r and total > 0:
                    ans = min(ans, total)

        if ans == float('inf'):
            return -1

        return ans
