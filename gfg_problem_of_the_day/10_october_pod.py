
class Solution:
    def balancePan(self, a, b):
        while b > 0:
            r = b % a

            if r != 0 and r != 1 and r != a - 1:
                return False

            if r == a - 1:
                b += 1

            b //= a

        return True
