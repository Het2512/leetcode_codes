class Solution:
    def maxPathSum(self, root):
        self.ans = float('-inf')

        def solve(node):
            if node is None:
                return float('-inf')

            # Leaf node
            if node.left is None and node.right is None:
                return node.data

            left = solve(node.left)
            right = solve(node.right)

            # If both children exist, this can form a leaf-to-leaf path
            if node.left is not None and node.right is not None:
                self.ans = max(
                    self.ans,
                    left + node.data + right
                )

                # Return best path from node to a leaf
                return node.data + max(left, right)

            # Only left child exists
            if node.left is not None:
                return node.data + left

            # Only right child exists
            return node.data + right

        solve(root)

        # Fewer than two leaves
        if self.ans == float('-inf'):
            return -1

        return self.ans