class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if s == ''.join(sorted(s)):
            return 0

        mn = min(s)
        mx = max(s)

        # If minimum occurs at the beginning OR maximum at the end
        if s[0] == mn or s[-1] == mx:
            return 1

        # Length 2 cannot be changed unless already sorted
        if n == 2:
            return -1

        # Check if minimum appears anywhere before the last position
        # OR maximum appears anywhere after the first position
        if mn in s[:-1] or mx in s[1:]:
            return 2

        return 3