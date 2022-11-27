def checkIfOk(a, b, c):
    if a + b == c or b + c == a or a + c == b:
        return True
    else:
        return False


n = int(input())
total = []

for i in range(n):
    arr = [int(x) for x in input().split()]
    total.append(arr)


for arr in total:
    if checkIfOk(arr[0], arr[1], arr[2]):
        print("YES")
    else:
        print("NO")
