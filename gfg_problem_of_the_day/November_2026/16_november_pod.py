
class Solution:
    def findKthSmall(self, arr, k):
        arr.sort()

        for i in range(len(arr)):
            missing = arr[i] - (i + 1)

            if missing >= k:
                return k + i

        return k + len(arr)
