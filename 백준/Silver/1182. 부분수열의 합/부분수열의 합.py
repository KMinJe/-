import sys

def dfs(p, sum):
    global cnt

    if sum == s and p >= 1:
        cnt += 1
    
    for i in range(p, n):
        sum += num_list[i]
        dfs(i + 1, sum)
        sum -= num_list[i]

n, s= map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

cnt = 0 
dfs(0, 0)
print(cnt)