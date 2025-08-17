import sys

n = int(sys.stdin.readline().strip())

stage_points = []

for _ in range(n):
    stage_points.append(int(sys.stdin.readline().strip()))

sum = 0
for stage_num in range(n-1, 0, -1):
    if stage_points[stage_num] <= stage_points[stage_num - 1]:
        change_gap = stage_points[stage_num - 1] - stage_points[stage_num] + 1
        sum += change_gap
        stage_points[stage_num - 1] -= change_gap
print(sum)