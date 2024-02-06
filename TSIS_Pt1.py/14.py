def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

def check_palindrome(word):
    return word == word[::-1]