
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Coordinate compression
        vals = sorted(set(nums))
        m = len(vals)
        rank = {v: i + 1 for i, v in enumerate(vals)}

        # Fenwick Trees: frequency and sum
        count = [0] * (m + 1)
        total = [0] * (m + 1)

        def update(bit, i, delta):
            while i <= m:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        # Find the index of kth smallest element
        def kth(kth_value):
            idx = 0
            bit_mask = 1 << (m.bit_length() - 1)

            while bit_mask:
                nxt = idx + bit_mask
                if nxt <= m and count[nxt] < kth_value:
                    idx = nxt
                    kth_value -= count[nxt]
                bit_mask >>= 1

            return idx + 1

        # Initialize first window
        window_sum = 0

        for i in range(x):
            v = nums[i]
            r = rank[v]
            update(count, r, 1)
            update(total, r, v)
            window_sum += v

        # Calculate minimum cost for every window
        costs = []

        for start in range(n - x + 1):

            # Median of current window
            mid = kth((x + 1) // 2)
            median = vals[mid - 1]

            left_count = query(count, mid)
            left_sum = query(total, mid)

            right_count = x - left_count
            right_sum = window_sum - left_sum

            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            costs.append(cost)

            # Slide window
            if start < n - x:
                old = nums[start]
                new = nums[start + x]

                update(count, rank[old], -1)
                update(total, rank[old], -old)

                update(count, rank[new], 1)
                update(total, rank[new], new)

                window_sum += new - old

        # DP: minimum cost to select k non-overlapping windows
        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Skip current element
                curr[i] = curr[i - 1]

                # Select window ending at i - 1
                if i >= x:
                    start = i - x
                    curr[i] = min(
                        curr[i],
                        prev[start] + costs[start]
                    )

            prev = curr

        return prev[n]
