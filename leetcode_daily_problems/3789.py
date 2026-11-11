
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        common = min(need1, need2)

        # Buy items that contribute to both requirements
        ans = common * min(costBoth, cost1 + cost2)

        # Remaining requirements
        rem1 = need1 - common
        rem2 = need2 - common

        # Fulfil remaining type 1 requirement
        ans += rem1 * min(cost1, costBoth)

        # Fulfil remaining type 2 requirement
        ans += rem2 * min(cost2, costBoth)

        return ans
