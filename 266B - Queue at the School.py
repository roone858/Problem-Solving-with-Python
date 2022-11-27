n, t = [int(x) for x in input().split()]
x = input()
queue = list(x)
while t > 0:
    i = 0
    while i < (len(queue) - 1):
        if queue[i] == 'B' and queue[i + 1] == 'G':
            queue[i], queue[i + 1] = queue[i + 1], queue[i]

            i += 1
        i += 1
    t -= 1
print("".join(queue))
