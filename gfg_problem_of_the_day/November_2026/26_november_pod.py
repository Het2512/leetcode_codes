
class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:

        vowels = "aeiou"
        prefix = [0] * (len(s) + 1)

        # Build prefix sum
        for i in range(len(s)):
            prefix[i + 1] = prefix[i] + (1 if s[i] in vowels else 0)

        # Answer queries
        ans = []

        for l, r in queries:
            count = prefix[r + 1] - prefix[l]
            ans.append(count)

        return ans
