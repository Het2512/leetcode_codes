
class Solution:
    def smallestSubWithSum(self, arr, x):
        left = 0
        curr_sum = 0
        ans = float('inf')

        for right in range(len(arr)):
            curr_sum += arr[right]

            while curr_sum > x:
                ans = min(ans, right - left + 1)
                curr_sum -= arr[left]
                left += 1

        if ans == float('inf'):
            return 0

        return ans
