
class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        k = totalTime
        window_sum = sum(arr[:k])
        max_sum = window_sum

        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum
