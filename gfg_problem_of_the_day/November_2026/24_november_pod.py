
class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:

        mp = {}
        all_pairs = []

        # Step 1: Generate all pairs and group by sum
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):

                s = arr[i] + arr[j]

                if s not in mp:
                    mp[s] = []

                pos = len(mp[s])
                mp[s].append((i, j))

                all_pairs.append((i, j, s, pos))

        # Step 2: Find lexicographically smallest valid quadruplet
        for a, b, s, pos in all_pairs:

            pairs = mp[s]

            # Check pairs appearing after (a, b)
            for c, d in pairs[pos + 1:]:

                # All four indices must be distinct
                if a != c and a != d and b != c and b != d:
                    return [a, b, c, d]

        return [-1, -1, -1, -1]
