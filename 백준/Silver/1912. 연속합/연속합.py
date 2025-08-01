import sys

n = int(sys.stdin.readline().strip())

num_list = list(map(int, sys.stdin.readline().split()))

num_position_sum = [0]
memo = [num_list[0]] * (n)
memo_max = memo[0]
min = num_list[0]

for _ in range(0,n):
    sum = num_position_sum[-1] + num_list[_]
    num_position_sum.append(sum)
    
    if _ > 0:
        memo[_] = max(memo[_ - 1], sum-min, sum)
        if memo[_] > memo_max:
            memo_max = memo[_]
    else:
        memo[_] = sum

    if sum < min:
        min = sum

print(memo_max)

