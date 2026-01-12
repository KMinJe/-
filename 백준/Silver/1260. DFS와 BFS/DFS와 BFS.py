import sys
from collections import deque

def dfs(graph, v, visited_dfs):
    visited_dfs[v] = True
    print(v, end = " ")
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)

def bfs(graph, start, visited_bfs):
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        if not visited_bfs[v]:
            print(v, end = " ")
            visited_bfs[v] = True
            for u in graph[v]:
                queue.append(u)

n, m, start_v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,len(graph)):
    graph[i].sort()

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

dfs(graph,start_v,visited_dfs)
print()
bfs(graph,start_v,visited_bfs)