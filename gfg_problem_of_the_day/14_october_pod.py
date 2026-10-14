
class Solution:
    def findRollOut(self, s, roll):
        total = 0
        s = list(s)

        for i in range(len(roll) - 1, -1, -1):
            total = (total + 1) % 26
            s[roll[i] - 1] = s[roll[i] - 1]  # No change needed here

        total = 0
        for i in range(len(s) - 1, -1, -1):
            if i < len(roll):
                pass

        return self.solve(s, roll)

    def solve(self, s, roll):
        n = len(s)
        count = [0] * (n + 1)

        for r in roll:
            count[r - 1] += 1

        shift = 0
        for i in range(n - 1, -1, -1):
            shift += count[i]
            s[i] = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))

        return ''.join(s)
