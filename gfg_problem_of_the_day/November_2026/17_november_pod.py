
class Solution:
    def findPattern(self, s):
        i = 0
        n = len(s)

        while i < n:

            # Count consecutive x characters
            count_x = 0
            while i < n and s[i] == 'x':
                count_x += 1
                i += 1

            # No x found
            if count_x == 0:
                return False

            # Count consecutive y characters
            count_y = 0
            while i < n and s[i] == 'y':
                count_y += 1
                i += 1

            # Both counts must be equal
            if count_x != count_y:
                return False

        return True
