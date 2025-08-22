import sys

n,m = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0

sum_position = [0]

for _ in num_list:
    sum_position.append(sum_position[-1] + _)

count = 0
while (start != n):
    if sum_position[end] - sum_position[start] == m:
        count += 1
        start += 1
    elif sum_position[end] - sum_position[start] < m:
        if end < n:
            end += 1
        else:
            start += 1
    else:
        start += 1

print(count)