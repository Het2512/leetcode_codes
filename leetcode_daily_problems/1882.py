
import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        available = []
        busy = []

        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        ans = []
        time = 0

        for i, duration in enumerate(tasks):

            time = max(time, i)

            # Release servers that have completed their tasks
            while busy and busy[0][0] <= time:
                end, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            # If no server is free, move time forward
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    end, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            # Get the server with minimum weight and index
            weight, idx = heapq.heappop(available)

            ans.append(idx)

            # Server becomes free after processing the task
            heapq.heappush(busy, (time + duration, weight, idx))

        return ans
