class Solution:
    def maximumSubarray(self, arr: list[int]) -> int:
        no_square = arr[0]
        one_square = arr[0] ** 2

        ans = one_square

        for i in range(1, len(arr)):
            x = arr[i]

            # Maximum subarray ending here without squaring
            no_square = max(x, no_square + x)

            # Maximum subarray ending here with one square
            one_square = max(
                x * x,
                no_square - x + x * x,
                one_square + x
            )

            ans = max(ans, no_square, one_square)

        return ans