import sys

n = int(sys.stdin.readline().strip())

A = list(map(int, sys.stdin.readline().split()))

B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort()
B.reverse()
sum = 0

for a,b in zip(A,B):
    sum += a * b

print(sum)


     