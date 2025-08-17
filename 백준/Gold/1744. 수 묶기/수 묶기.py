import sys

n = int(sys.stdin.readline().strip())

num_list_positive = []
num_list_negative = []
num_list_zero = []
num_list_one = []
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num > 1:
        num_list_positive.append(num)
    elif num < 0:
        num_list_negative.append(num)
    elif num == 1:
        num_list_one.append(num)
    else:
        num_list_zero.append(num)

num_list_positive.sort(reverse=True)
num_list_negative.sort()
sum = 0
while len(num_list_negative) > 1:
    a = num_list_negative.pop(0)
    b = num_list_negative.pop(0)
    sum += a * b

if len(num_list_zero) == 0 and num_list_negative:
    sum += num_list_negative.pop(0)

while len(num_list_positive) > 1:
    a = num_list_positive.pop(0)
    b = num_list_positive.pop(0)
    sum += a * b

if num_list_positive:
    sum += num_list_positive.pop(0)

if num_list_one:
    sum += len(num_list_one)

print(sum)