
class Solution:
    def checkWithinK(self, arr: list[int], k: int) -> bool:
        seen = set()

        for i in range(len(arr)):
            if arr[i] in seen:
                return True

            seen.add(arr[i])

            if i >= k:
                seen.remove(arr[i - k])

        return False
