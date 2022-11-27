n = int(input())
count = int(0)
inside = int(0)
for i in range(n):
    if inside < int(0):
        inside = int(0)
    exit, enter = [int(x) for x in input().split()]
    inside = (inside - exit) + enter
    if inside > count:
        count = inside
print(count)
