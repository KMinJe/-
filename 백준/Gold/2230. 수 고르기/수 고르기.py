import sys

n,m = map(int, sys.stdin.readline().split())

num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline().strip()))

num_list.sort()

minimum = 2000000000
start = 0 
end = 0

if n > 1:
    while (start < n):
        if abs(num_list[start] - num_list[end]) >= m:
            minimum = min(minimum, abs(num_list[start] - num_list[end]))
            if end < n-1:
                end += 1
            else:
                start +=1
        else:
            start += 1
else:
    minimum = m

print(minimum)