class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        # Always use the faster scanner first
        if s1 > s2:
            s1, s2 = s2, s1

        low = 0
        high = n * s1

        while low < high:
            mid = (low + high) // 2

            # Documents scanned by each scanner within mid time
            total = (mid // s1) + (mid // s2)

            if total >= n:
                high = mid
            else:
                low = mid + 1

        return low