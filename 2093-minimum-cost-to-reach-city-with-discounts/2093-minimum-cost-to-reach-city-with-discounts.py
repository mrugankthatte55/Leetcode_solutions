class Solution:
    def minimumCost(
        self, n: int, highways: List[List[int]], discounts: int
    ) -> int:
        graph = [[] for _ in range(n)]
        for highway in highways:
            u, v, toll = highway
            graph[u].append((v, toll))
            graph[v].append((u, toll))
        pq = [(0, 0, 0)] 
        dist = [[float("inf")] * (discounts + 1) for _ in range(n)]
        dist[0][0] = 0

        while pq:
            current_cost, city, discounts_used = heapq.heappop(pq)
            if current_cost > dist[city][discounts_used]:
                continue
            for neighbor, toll in graph[city]:
                if current_cost + toll < dist[neighbor][discounts_used]:
                    dist[neighbor][discounts_used] = current_cost + toll
                    heapq.heappush(
                        pq,
                        (
                            dist[neighbor][discounts_used],
                            neighbor,
                            discounts_used,
                        ),
                    )
                if discounts_used < discounts:
                    new_cost_with_discount = current_cost + toll // 2
                    if (
                        new_cost_with_discount
                        < dist[neighbor][discounts_used + 1]
                    ):
                        dist[neighbor][
                            discounts_used + 1
                        ] = new_cost_with_discount
                        heapq.heappush(
                            pq,
                            (
                                new_cost_with_discount,
                                neighbor,
                                discounts_used + 1,
                            ),
                        )
        min_cost = min(dist[n - 1])
        return -1 if min_cost == float("inf") else min_cost