
class Solution:
    def largestSumCycle(self, edge):
        n = len(edge)

        visited = [False] * n
        ans = -1

        for i in range(n):
            if visited[i]:
                continue

            curr = i
            path = {}
            steps = 0

            while curr != -1 and not visited[curr]:
                visited[curr] = True
                path[curr] = steps
                steps += 1

                curr = edge[curr]

            # Check if a cycle exists in the current path
            if curr != -1 and curr in path:

                cycle_sum = sum(
                    node for node in path
                    if path[node] >= path[curr]
                )

                ans = max(ans, cycle_sum)

        return ans
