from collections import deque
import sys

n, k= map(int, sys.stdin.readline().split())

M = 100000

visited = [False] * (M + 1)
parents = [-1] * (M + 1)

def bfs():
    d=deque()
    d.append((n,1))

    if n == k:
        return 0
    
    while d:
        x,y = d.popleft()

        for _ in range(3):
            if _ == 0:
                nx = x + 1
            elif _ == 1:
                nx = x - 1
            else:
                nx = x * 2

            if nx < 0 or nx > M:
                continue

            if visited[nx]:
                continue
            
            visited[nx] = True
            parents[nx] = x
            if nx == k:
                return y

            d.append((nx,y + 1))
                     
print(bfs())
path = deque()
p = k
while p != n:
    path.append(p)
    p = parents[p]
print (n, end=' ')
while path:
    print(path.pop(), end=' ')