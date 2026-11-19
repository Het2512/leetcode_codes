class Solution:
    def sortIt(self, arr):
        odd = []
        even = []

        for num in arr:
            if num % 2 == 1:
                odd.append(num)
            else:
                even.append(num)

        odd.sort(reverse=True)
        even.sort()

        arr[:] = odd + even