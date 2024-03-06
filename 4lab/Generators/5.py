def nums(n):
    for i in range(n,-1, -1):
        yield i
nums = nums(int(input()))
for i in nums:
    print(i)