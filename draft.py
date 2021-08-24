nums = [int(i) for i in input().split()]
for i in range(1, len(nums)):
    if i % 2 != 0:
        nums[i], nums[i-1] = nums[i-1], nums[i]
print(*nums)
