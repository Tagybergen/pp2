def squares_generator(N):
    for i in range(1, N+1):
        yield i**2
n=int(input())
for square in squares_generator(n):
    print(square)
5