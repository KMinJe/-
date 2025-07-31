import sys

n = int(sys.stdin.readline().strip())

memo = [0] * (10**6 + 1)

memo[1] = 0
memo[2] = 1
memo[3] = 1

for _ in range(1,n+1):
    if _ > 3:
        if _ % 6 == 0:
            memo[_] = min(memo[_//3]+1, memo[_//2]+1, memo[_-1]+1)
        elif _ % 3 == 0:
            memo[_] = min(memo[_//3]+1, memo[_-1]+1)
        elif _ % 2 == 0:
            memo[_] = min(memo[_//2]+1, memo[_-1]+1)
        else:
            memo[_] = memo[_-1]+1

print(memo[n])