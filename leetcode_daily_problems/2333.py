
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if k >= sum(diff):
            return 0

        left, right = 0, max(diff)

        # Find the smallest maximum difference possible
        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        limit = left

        # Reduce every difference to at most limit
        used = sum(max(0, d - limit) for d in diff)
        remaining = k - used

        ans = 0

        for d in diff:
            d = min(d, limit)

            # Use remaining operations on differences equal to limit
            if d == limit and remaining > 0:
                d -= 1
                remaining -= 1

            ans += d * d

        return ans
