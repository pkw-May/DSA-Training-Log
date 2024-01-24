import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
visited = [0] * (V+1)

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))
    graph[end].append((cost, start))


def prim(graph, startNode):
    visited[startNode] = 1
    adjNodes = graph[startNode]

    heapq.heapify(adjNodes)
    totalCost = 0

    while adjNodes:
        cost, endNode = heapq.heappop(adjNodes)

        if visited[endNode] == 0:
            visited[endNode] = 1
            totalCost += cost

            for edge in graph[endNode]:
                if visited[edge[1]] == 0:
                    heapq.heappush(adjNodes, edge)

    return totalCost

print(prim(graph, 1))
