
class Solution:
    def checkPath(self, adj: list[list[int]], u: int, v: int) -> bool:

        visited = [False] * len(adj)

        def dfs(node):

            if node == v:
                return True

            visited[node] = True

            for neighbour in adj[node]:

                if not visited[neighbour]:

                    if dfs(neighbour):
                        return True

            return False

        return dfs(u)
