import sys

n = int(sys.stdin.readline().strip())

def prime(k):
    prime = [True] * (k + 1)
    m = k ** 0.5
    result = []
    for i in range(2, int(m) + 1):
        if prime[i]:
            for j in range(2 * i, k+1, i):
                prime[j] = False
    for i in range(2, k + 1):
        if prime[i]:
            result.append(i)
    return result

prime_list = prime(n)

sum_prime = [0]

for _ in prime_list:
    sum_prime.append(sum_prime[-1] + _)

start = 0
end = 1

count = 0
while (start != len(sum_prime)-1):
    if sum_prime[end] - sum_prime[start] == n:
        count += 1
        start += 1
    elif sum_prime[end] - sum_prime[start] < n:
        if end < len(sum_prime)-1:
            end += 1
        else:
            start += 1
    else:
        start += 1

print(count)