# import sys
# from collections import deque 
# def bfs(graph, start, visited_bfs):
#     queue = deque()
#     queue.append(start)
#     depth = 1
#     global num_connection_with_one
#     while queue:
#         v = queue.popleft()
#         if not visited_bfs[v]:
#             visited_bfs[v] = True
#             print(v)
#             num_connection_with_one += 1
#             for u in graph[v]:
#                 queue.append(u)
#         depth+=1

#         if depth == len(graph[1])+2:
#             break

# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline()) 

# graph = [[] for _ in range(n+1)]
# for i in range(m):
#     u, v = map(int, sys.stdin.readline().split())
#     graph[u].append(v)
#     graph[v].append(u)


# visited_bfs = [False] * (n+1)
# num_connection_with_one = 0
# print(graph)
# bfs(graph, 1, visited_bfs)

# print(num_connection_with_one - 1)


import sys
from collections import deque 
n = int(sys.stdin.readline())
m = int(sys.stdin.readline()) 

graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

num_connection_with_one = set()
for _ in graph[1]:
    num_connection_with_one.add(_)
    for i in graph[_]:
        num_connection_with_one.add(i)

if len(num_connection_with_one) == 0:
    print(0)
else:
    print(len(num_connection_with_one)- 1)
