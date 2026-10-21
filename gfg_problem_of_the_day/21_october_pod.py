class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        curr_sum = arr[0]
        min_sum = arr[0]

        for i in range(1, len(arr)):
            curr_sum = min(arr[i], curr_sum + arr[i])
            min_sum = min(min_sum, curr_sum)

        return min_sum