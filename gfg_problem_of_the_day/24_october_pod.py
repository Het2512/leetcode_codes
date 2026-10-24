class Solution:
    def isPossible(self, n, m, s):
        x = y = 0
        min_x = max_x = 0
        min_y = max_y = 0

        for ch in s:
            if ch == 'L':
                y -= 1
            elif ch == 'R':
                y += 1
            elif ch == 'D':
                x -= 1
            elif ch == 'U':
                x += 1

            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

        return (max_x - min_x < n and
                max_y - min_y < m)