n, k = [int(x) for x in input().split()]
count = 0
nums = [int(x) for x in input().split()]

for i in range(n):
    if nums[i] >= k:
        count = count + 1
    for j in range(i + 1, n):
        if nums[i] + nums[j] >= k > nums[i] and nums[j] < k:
            count = count + 1
print(count)
