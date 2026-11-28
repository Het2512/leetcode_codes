
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        n = len(items)

        freq = [0] * (n + 1)

        min_price = float('inf')

        # Step 1: Count frequency of each factor
        for factor, price in items:
            freq[factor] += 1
            min_price = min(min_price, price)

        # Step 2: Count items divisible by each factor
        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i):
                freq[i] += freq[j]

        # Step 3: Create useful purchase opportunities
        deals = []

        for factor, price in items:

            gain = freq[factor] - 1

            if gain > 0 and price <= 2 * min_price:
                deals.append((price, gain))

        # Step 4: Sort by price
        deals.sort()

        ans = 0

        # Step 5: Buy useful copies first
        for price, gain in deals:

            take = min(gain, budget // price)

            ans += take * 2
            budget -= take * price

        # Step 6: Buy normal copies with remaining budget
        ans += budget // min_price

        return ans
