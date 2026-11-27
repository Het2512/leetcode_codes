
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)

        # Step 1: Count frequency of each factor
        mx = max(f for f, p in items)

        freq = [0] * (mx + 1)

        for f, p in items:
            freq[f] += 1

        # Step 2: Count how many factors are divisible
        divisible = [0] * (mx + 1)

        for f in range(1, mx + 1):
            for j in range(f, mx + 1, f):
                divisible[f] += freq[j]

        # Step 3: Initialize DP
        dp = [-float('inf')] * (budget + 1)
        dp[0] = 0

        # Step 4: Process each item
        for f, p in items:

            bonus = divisible[f] - 1

            new_dp = dp[:]

            # Process each remainder
            for r in range(p):
                best = -float('inf')

                t = 0
                b = r

                while b <= budget:

                    # Buy at least one copy
                    if best != -float('inf'):
                        new_dp[b] = max(
                            new_dp[b],
                            bonus + t + best
                        )

                    # Update running maximum
                    best = max(best, dp[b] - t)

                    b += p
                    t += 1

            dp = new_dp

        return max(dp)
