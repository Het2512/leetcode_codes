
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Step 1: Prefix sum
        pref = [0] * (n + 1)

        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        # Step 2: Next Greater Element
        nxt = [n] * n
        st = []

        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()

            if st:
                nxt[i] = st[-1]

            st.append(i)

        # Step 3: Binary Lifting
        LOG = n.bit_length()

        up = [[n] * n for _ in range(LOG)]
        sm = [[0] * n for _ in range(LOG)]

        for i in range(n):
            up[0][i] = nxt[i]
            sm[0][i] = nums[i] * (nxt[i] - i)

        for p in range(1, LOG):
            for i in range(n):
                mid = up[p - 1][i]

                if mid < n:
                    up[p][i] = up[p - 1][mid]
                    sm[p][i] = sm[p - 1][i] + sm[p - 1][mid]

        # Step 4: Calculate operations
        def getCost(l, r):
            cur = l
            total = 0

            for p in range(LOG - 1, -1, -1):
                pos = up[p][cur]

                if pos <= r:
                    total += sm[p][cur]
                    cur = pos

            total += nums[cur] * (r - cur + 1)

            return total - (pref[r + 1] - pref[l])

        # Step 5: Two Pointers
        ans = 0
        r = 0

        for l in range(n):
            while r + 1 < n and getCost(l, r + 1) <= k:
                r += 1

            ans += r - l + 1

        return ans
