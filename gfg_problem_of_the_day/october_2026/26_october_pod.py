
class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        n = len(arr)

        if k == 0:
            return max(arr) - min(arr)

        if k == n - 1:
            return 0

        left_min = [0] * n
        left_max = [0] * n
        right_min = [0] * n
        right_max = [0] * n

        left_min[0] = left_max[0] = arr[0]

        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], arr[i])
            left_max[i] = max(left_max[i - 1], arr[i])

        right_min[n - 1] = right_max[n - 1] = arr[n - 1]

        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], arr[i])
            right_max[i] = max(right_max[i + 1], arr[i])

        ans = float('inf')

        for i in range(n - k + 1):
            l = i - 1
            r = i + k

            if l < 0:
                mn = right_min[r]
                mx = right_max[r]
            elif r >= n:
                mn = left_min[l]
                mx = left_max[l]
            else:
                mn = min(left_min[l], right_min[r])
                mx = max(left_max[l], right_max[r])

            ans = min(ans, mx - mn)

        return ans
