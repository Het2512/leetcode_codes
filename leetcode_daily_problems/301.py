class Solution:
    def removeInvalidParentheses(self, s):
        # Find minimum number of left and right parentheses to remove
        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def backtrack(index, left_count, right_count,
                      left_remove, right_remove, path):

            # End of string
            if index == len(s):
                if left_remove == 0 and right_remove == 0:
                    result.add("".join(path))
                return

            ch = s[index]

            # Option 1: Remove this parenthesis
            if ch == '(' and left_remove > 0:
                backtrack(
                    index + 1,
                    left_count,
                    right_count,
                    left_remove - 1,
                    right_remove,
                    path
                )

            elif ch == ')' and right_remove > 0:
                backtrack(
                    index + 1,
                    left_count,
                    right_count,
                    left_remove,
                    right_remove - 1,
                    path
                )

            # Option 2: Keep this character
            if ch not in '()':
                path.append(ch)

                backtrack(
                    index + 1,
                    left_count,
                    right_count,
                    left_remove,
                    right_remove,
                    path
                )

                path.pop()

            elif ch == '(':
                path.append(ch)

                backtrack(
                    index + 1,
                    left_count + 1,
                    right_count,
                    left_remove,
                    right_remove,
                    path
                )

                path.pop()

            elif ch == ')':
                # We can only keep ')' if there is an unmatched '('
                if left_count > right_count:
                    path.append(ch)

                    backtrack(
                        index + 1,
                        left_count,
                        right_count + 1,
                        left_remove,
                        right_remove,
                        path
                    )

                    path.pop()

        backtrack(
            0,
            0,
            0,
            left_remove,
            right_remove,
            []
        )

        return list(result)