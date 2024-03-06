def is_palindrome(text):
    text = text.lower()
    inverse=text[::-1]
    return text == text[::-1]

input_string = input()

if is_palindrome(input_string):
    print("YES")
else:
    print("NO")
