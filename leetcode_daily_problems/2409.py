class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:

        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        def getDay(date):
            month, day = map(int, date.split("-"))
            return sum(days[:month - 1]) + day

        alice_start = getDay(arriveAlice)
        alice_end = getDay(leaveAlice)

        bob_start = getDay(arriveBob)
        bob_end = getDay(leaveBob)

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)

        return max(0, end - start + 1)