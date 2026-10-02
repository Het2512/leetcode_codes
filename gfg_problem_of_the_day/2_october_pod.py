class Solution:
    def lexiString(self, s):
        n = len(s)

        ss = s + s

        i = 0
        j = 1
        k = 0

        while i < n and j < n and k < n:

            if ss[i + k] == ss[j + k]:
                k += 1

            elif ss[i + k] > ss[j + k]:
                i = i + k + 1

                if i <= j:
                    i = j + 1

                k = 0

            else:
                j = j + k + 1

                if j <= i:
                    j = i + 1

                k = 0

        start = min(i, j)

        return ss[start:start + n]