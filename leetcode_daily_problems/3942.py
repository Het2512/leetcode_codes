from collections import deque

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        # Already sorted
        if nums == list(range(n)):
            return 0

        rev = nums[::-1]

        # Find the shift that sorts each base array, if one exists.
        targets = set()

        for t, arr in enumerate((nums, rev)):
            k = arr.index(0)

            # Check whether rotating left by k gives sorted order.
            if all(arr[(k + i) % n] == i for i in range(n)):
                targets.add((t, k))

        # Not a rotation of increasing or decreasing order
        if not targets:
            return -1

        # State = (type, shift)
        # type 0: rotation of nums
        # type 1: rotation of reversed nums
        q = deque([(0, 0, 0)])  # type, shift, distance
        visited = {(0, 0)}

        while q:
            t, shift, dist = q.popleft()

            if (t, shift) in targets:
                return dist

            # Operation 1: rotate left by one
            ns = (shift + 1) % n
            state = (t, ns)

            if state not in visited:
                visited.add(state)
                q.append((t, ns, dist + 1))

            # Operation 2: reverse the entire array
            nt = 1 - t
            ns = (-shift) % n
            state = (nt, ns)

            if state not in visited:
                visited.add(state)
                q.append((nt, ns, dist + 1))

        return -1