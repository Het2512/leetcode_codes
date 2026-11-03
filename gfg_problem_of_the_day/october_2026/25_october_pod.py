
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total = 0

        for i in range(n):
            freq = [0] * 26
            max_freq = 0

            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1

                if freq[idx] > max_freq:
                    max_freq = freq[idx]

                min_freq = n

                for k in range(26):
                    if freq[k] > 0 and freq[k] < min_freq:
                        min_freq = freq[k]

                total += max_freq - min_freq

        return total
