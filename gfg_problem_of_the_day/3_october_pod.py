class Solution:
    def formCoils(self, n):
        size = 4 * n

        # Create matrix
        matrix = [[0] * size for _ in range(size)]

        value = 1
        for i in range(size):
            for j in range(size):
                matrix[i][j] = value
                value += 1

        # ------------------------------------------------
        # FIRST COIL
        # ------------------------------------------------
        coil1 = []
        visited = [[False] * size for _ in range(size)]

        top = 0
        left = 0
        bottom = size - 1
        right = size - 1

        while bottom - top + 1 >= 4:

            # Down along left side
            for i in range(top, bottom + 1):
                coil1.append(matrix[i][left])
                visited[i][left] = True

            # Right along bottom
            for j in range(left + 1, right):
                coil1.append(matrix[bottom][j])
                visited[bottom][j] = True

            # Up along inner-right side
            for i in range(bottom - 1, top, -1):
                coil1.append(matrix[i][right - 1])
                visited[i][right - 1] = True

            # Left along inner-top side
            for j in range(right - 2, left + 1, -1):
                coil1.append(matrix[top + 1][j])
                visited[top + 1][j] = True

            # Move two cells inward
            top += 2
            left += 2
            bottom -= 2
            right -= 2

        # ------------------------------------------------
        # SECOND COIL
        # ------------------------------------------------
        coil2 = []

        # Start from bottom-right
        r = size - 1
        c = size - 1

        # Up, Left, Down, Right
        directions = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        d = 0
        total = (size * size) // 2

        while len(coil2) < total:

            coil2.append(matrix[r][c])
            visited[r][c] = True

            nr = r + directions[d][0]
            nc = c + directions[d][1]

            # Turn if next cell is outside matrix
            # or already belongs to first coil / second coil
            if (nr < 0 or nr >= size or
                nc < 0 or nc >= size or
                visited[nr][nc]):

                d = (d + 1) % 4

                nr = r + directions[d][0]
                nc = c + directions[d][1]

            r = nr
            c = nc

        return [coil1, coil2]