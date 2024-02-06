def solve(numheads, numlegs):
    rabbits = numlegs // 2 - numheads 
    chikens = numheads - rabbits
    if numheads and numlegs:
        print(rabbits, chikens)
    else:
        print("No solution")

solve(35, 94)