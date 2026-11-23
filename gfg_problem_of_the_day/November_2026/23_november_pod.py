
class Solution:
    def posInfinite(self, s: str, pos: int) -> str:

        # Step 1: Calculate lengths
        lengths = [len(s)]
        i = 1

        while lengths[-1] < pos:
            new_len = 2 * lengths[-1] + i
            lengths.append(new_len)
            i += 1

        # Step 2: Traverse backwards
        for i in range(len(lengths) - 1, 0, -1):

            prev = lengths[i - 1]

            # Position is in reversed string
            if pos > prev + i:
                pos = lengths[i] - pos + 1

            # Position is in '$' section
            elif pos > prev:
                return '$'

            # Otherwise, position is in original string

        # Step 3: Return character from original string
        return s[pos - 1]
