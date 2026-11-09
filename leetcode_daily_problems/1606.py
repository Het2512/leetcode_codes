
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        # Fenwick Tree: initially all servers are available
        tree = [0] * (k + 1)

        for i in range(1, k + 1):
            tree[i] = i & -i

        def update(i, val):
            i += 1
            while i <= k:
                tree[i] += val
                i += i & -i

        def query(i):
            total = 0
            while i > 0:
                total += tree[i]
                i -= i & -i
            return total

        # Find the server with given rank (1-indexed)
        def find_server(rank):
            idx = 0
            bit = 1 << (k.bit_length() - 1)

            while bit:
                nxt = idx + bit
                if nxt <= k and tree[nxt] < rank:
                    idx = nxt
                    rank -= tree[nxt]
                bit >>= 1

            return idx

        busy = []  # (finish_time, server_id)
        count = [0] * k

        for i in range(len(arrival)):

            # Release servers that have completed their requests
            while busy and busy[0][0] <= arrival[i]:
                end, server = heapq.heappop(busy)
                update(server, 1)

            # Number of available servers
            total = query(k)

            if total == 0:
                continue

            start = i % k

            # Find available server >= start
            before = query(start)

            if before < total:
                server = find_server(before + 1)
            else:
                # Wrap around to the first available server
                server = find_server(1)

            # Assign request
            count[server] += 1
            update(server, -1)

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        # Find maximum number of requests handled
        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
