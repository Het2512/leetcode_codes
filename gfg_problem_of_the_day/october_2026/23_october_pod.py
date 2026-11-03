class Solution:
    def pairsViolatingBST(self, root):
        from bisect import bisect_left, bisect_right

        def solve(node):
            if not node:
                return [], 0

            left, left_bad = solve(node.left)
            right, right_bad = solve(node.right)

            bad = left_bad + right_bad

            # Violations involving the current node
            bad += len(left) - bisect_right(left, node.data)
            bad += bisect_left(right, node.data)

            # Cross-subtree violations:
            # count pairs (x, y) where x is in left subtree,
            # y is in right subtree, and x > y.
            j = 0
            for x in left:
                while j < len(right) and right[j] < x:
                    j += 1
                bad += j

            # Merge sorted arrays
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            merged.append(node.data)
            merged.sort()

            return merged, bad

        return solve(root)[1]