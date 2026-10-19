
class Solution:
    def goodIndices(self, arr):
        n = len(arr)
        state = [0] * n
        # 0 = unvisited, 1 = visiting, 2 = good, 3 = bad

        def dfs(i):
            # Jumped outside the array: good
            if i < 0 or i >= n:
                return True

            # Reached an index already being explored: cycle
            if state[i] == 1:
                return False

            # Previously calculated result
            if state[i] == 2:
                return True
            if state[i] == 3:
                return False

            state[i] = 1

            # Calculate next index
            next_i = i + arr[i]

            result = dfs(next_i)

            # Store the result
            state[i] = 2 if result else 3

            return result

        count = 0

        for i in range(n):
            if state[i] == 0:
                if dfs(i):
                    count += 1
            elif state[i] == 2:
                count += 1

        return count
