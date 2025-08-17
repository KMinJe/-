import sys

n = int(sys.stdin.readline().strip())

num_list = (list(map(int, sys.stdin.readline().strip().split())))

num_list.sort()

x = int(sys.stdin.readline().strip())

start = 0
end =  n - 1
total = 0
while start < end:
    sum = num_list[start] + num_list[end]
    if sum == x:
        total += 1
        start += 1
        end -= 1
    else:
        if sum < x:
            start += 1
        else:
            end -= 1
print(total)