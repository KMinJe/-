from collections import deque
import sys


n, m = map(int, sys.stdin.readline().split())

l = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

mx = [-1,1,0,0]
my = [0,0,-1,1]

def bfs():
    d=deque()
    d.append((0,0))

    while d:
        x,y = d.popleft()

        for _ in range(4):
            nx = x + mx[_]
            ny = y + my[_]

            if (nx < 0) or (ny < 0) or (nx >= n) or (ny >= m):
                continue
                
            if l[nx][ny] == 0:
                continue

            if l[nx][ny] == 1:
                l[nx][ny] = l[x][y] + 1
                d.append((nx,ny))

    return l[n-1][m-1]

print(bfs())
