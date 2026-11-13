
class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        s1 = []
        s2 = []
        ans = []

        while True:
            # Push all left nodes of first BST
            while r1:
                s1.append(r1)
                r1 = r1.left

            # Push all left nodes of second BST
            while r2:
                s2.append(r2)
                r2 = r2.left

            # If either stack is empty, traversal is complete
            if not s1 or not s2:
                break

            # Get the smallest unprocessed values
            top1 = s1[-1]
            top2 = s2[-1]

            if top1.data == top2.data:
                ans.append(top1.data)

                r1 = s1.pop().right
                r2 = s2.pop().right

            elif top1.data < top2.data:
                r1 = s1.pop().right

            else:
                r2 = s2.pop().right

        return ans
