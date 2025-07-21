from queue import PriorityQueue
import sys

n, k= map(int, sys.stdin.readline().split())

M = 100000
visited = [False] * (M + 1)
mx = [2, 1, -1]
def bfs():

    d=PriorityQueue()
    d.put((0,n))
    visited[n] = True
    
    if n == k:
        return 0
    
    while not d.empty():
        y,x = d.get()

        for _ in range(3):
            if _ == 0:
                nx = x * 2

                if nx < 0 or nx > M:
                    continue

                if visited[nx]:
                    continue
                
                visited[nx] = True

                if nx == k:
                    return y

                d.put((y,nx))
            else:
                nx = x + mx[_]

                if nx < 0 or nx > M:
                    continue

                if visited[nx]:
                    continue
                
                visited[nx] = True

                if nx == k:
                    return (y+1)

                d.put((y + 1,nx))

print(bfs())