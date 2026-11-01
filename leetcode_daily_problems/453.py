
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mini = min(nums)
        ans = 0

        for num in nums:
            ans += num - mini

        return ans
