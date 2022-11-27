n, k = [int(x) for x in input().split()]
difRates = []
studentId = []
rates = [int(x) for x in input().split()]
for i in range(len(rates)):
    if rates[i] not in difRates:
        difRates.append(rates[i])
        studentId.append(str(i+1))

if len(difRates) >= k:
    print("YES")
    print(' '.join(studentId[slice(k)]))
else:
    print("NO")
