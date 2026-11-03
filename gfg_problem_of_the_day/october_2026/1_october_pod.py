from collections import deque

class Solution:
    def minTime(self, duration, dependencies):
        n = len(duration)

        adj = [[] for _ in range(n)]
        indegree = [0] * n

        # Build graph
        for u, v in dependencies:
            adj[u].append(v)
            indegree[v] += 1

        # dp[i] = earliest time module i is completed
        dp = [0] * n

        q = deque()

        # Modules with no dependencies
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                dp[i] = duration[i]

        count = 0
        answer = 0

        while q:
            u = q.popleft()
            count += 1

            answer = max(answer, dp[u])

            for v in adj[u]:
                dp[v] = max(dp[v], dp[u] + duration[v])

                indegree[v] -= 1

                if indegree[v] == 0:
                    q.append(v)

        # Cycle exists
        if count != n:
            return -1

        return answer