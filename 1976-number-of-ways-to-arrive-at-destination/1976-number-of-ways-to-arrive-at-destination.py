class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        heap = [(0, 0)]
        
        while heap:
            curr_time, u = heapq.heappop(heap)
            
            if curr_time > dist[u]:
                continue
            
            for v, time in graph[u]:
                new_time = curr_time + time
                if new_time < dist[v]:
                    dist[v] = new_time
                    ways[v] = ways[u]
                    heapq.heappush(heap, (new_time, v))
                elif new_time == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        
        return ways[n - 1]
