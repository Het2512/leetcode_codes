
class Solution:
    def maximumWeight(self, n, edges, queries):
        
        # Sort edges by weight
        edges.sort(key=lambda x: x[2])
        
        # Store queries with their original indices
        q = sorted([(x, i) for i, x in enumerate(queries)])
        
        # DSU initialization
        parent = list(range(n + 1))
        size = [1] * (n + 1)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(u, v):
            ru = find(u)
            rv = find(v)
            
            if ru == rv:
                return 0
            
            # Union by size
            if size[ru] < size[rv]:
                ru, rv = rv, ru
            
            # Number of new paths
            paths = size[ru] * size[rv]
            
            parent[rv] = ru
            size[ru] += size[rv]
            
            return paths
        
        ans = [0] * len(queries)
        total = 0
        j = 0
        
        # Process queries in sorted order
        for x, idx in q:
            
            while j < len(edges) and edges[j][2] <= x:
                u, v, w = edges[j]
                
                total += union(u, v)
                j += 1
            
            ans[idx] = total
        
        return ans
