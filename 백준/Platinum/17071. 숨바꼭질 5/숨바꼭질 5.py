from collections import deque
import sys

n, k= map(int, sys.stdin.readline().split())

M = 500000
visited = [[-1,-1] for _ in range(M+1)]
        
visited[n][0] = 0
q = deque()
q.append((n))
time = 1
check = False
if n == k:
    time = 0
    check= True
else:
    while k<M+1:
        s=len(q)
        for _ in range(s):
            current = q.popleft()

            for next in (current*2, current-1, current+1):
                if next < 0 or next > M or visited[next][time % 2] != -1:
                    continue

                visited[next][time % 2] = 1
                q.append(next)
        k+=time
        if k<M+1:
            if visited[k][time % 2] > -1:
                check = True
                break
            time += 1

if check:
    print(time)
else:
    print(-1)