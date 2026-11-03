class Solution:
    def socialNetwork(self, arr):
        n = len(arr) + 1
        ans = []

        for i in range(2, n + 1):
            reachable = {}

            current = i
            distance = 0

            while current > 1:
                friend = arr[current - 2]
                distance += 1

                reachable[friend] = distance
                current = friend

            # j must be considered in increasing order
            for j in range(1, i):
                if j in reachable:
                    ans.append([i, j, reachable[j]])

        return ans