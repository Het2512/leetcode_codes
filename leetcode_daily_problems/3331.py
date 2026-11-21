
class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        # Step 1: Build original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Step 2: Find new parent using DFS
        new_parent = parent[:]

        last = [-1] * 26

        stack = [(0, False, -1)]

        while stack:
            node, exiting, old = stack.pop()

            idx = ord(s[node]) - ord('a')

            if exiting:
                last[idx] = old
                continue

            old = last[idx]

            if old != -1:
                new_parent[node] = old

            last[idx] = node

            stack.append((node, True, old))

            for child in reversed(children[node]):
                stack.append((child, False, -1))

        # Step 3: Build modified tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Step 4: Calculate subtree sizes
        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_children[node]:
                stack.append(child)

        ans = [1] * n

        for node in reversed(order[1:]):
            ans[new_parent[node]] += ans[node]

        return ans
