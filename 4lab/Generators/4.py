def squares(a,b):
    for i in range(a,b+1):
        yield i**2

nums = squares(int(input()), int(input()))
for i in nums:
    print(i)