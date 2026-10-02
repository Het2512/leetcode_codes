class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current, opening, closing):
            # We have used all n pairs
            if len(current) == 2 * n:
                result.append(current)
                return

            # We can add '(' if we haven't used all opening brackets
            if opening < n:
                backtrack(current + "(", opening + 1, closing)

            # We can add ')' only if there is an unmatched '('
            if closing < opening:
                backtrack(current + ")", opening, closing + 1)

        backtrack("", 0, 0)

        return result