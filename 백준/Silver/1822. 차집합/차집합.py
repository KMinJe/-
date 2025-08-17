import sys

n_A, n_B = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))

B = set(map(int, sys.stdin.readline().split()))

if (A - B):
    print(len(A - B))
    l = list(A - B)
    l.sort()
    for _ in l:
        print(_, end=' ')
else:
    print(0)