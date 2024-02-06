from itertools import permutations

def print_permutations(s):
    perms = [''.join(p) for p in permutations(s)]
    for perm in perms:
        print(perm)

input_str = input("Enter a string: ")

print_permutations(input_str)
