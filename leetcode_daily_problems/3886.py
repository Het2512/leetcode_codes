class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)

        def is_rotation(block, pattern):
            k = len(block)

            # KMP LPS array
            lps = [0] * k
            j = 0

            for i in range(1, k):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j - 1]

                if pattern[i] == pattern[j]:
                    j += 1

                lps[i] = j

            # Search pattern in two copies of the block
            j = 0

            for i in range(2 * k - 1):
                value = block[i % k]

                while j > 0 and value != pattern[j]:
                    j = lps[j - 1]

                if value == pattern[j]:
                    j += 1

                if j == k:
                    return True

            return False

        answer = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                pattern = sorted_nums[start:start + k]

                if not is_rotation(block, pattern):
                    valid = False
                    break

            if valid:
                answer += k

        return answer