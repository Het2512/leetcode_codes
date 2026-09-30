class Solution:
    def exclusiveTime(self, n, logs):
        ans = [0] * n
        stack = []
        prevTime = 0

        for log in logs:
            id, typ, time = log.split(":")
            id = int(id)
            time = int(time)

            if typ == "start":
                # Current function gets CPU time before this new function starts
                if stack:
                    ans[stack[-1]] += time - prevTime

                stack.append(id)
                prevTime = time

            else:
                # Current function runs until the END of this timestamp
                ans[stack[-1]] += time - prevTime + 1

                stack.pop()
                prevTime = time + 1

        return ans