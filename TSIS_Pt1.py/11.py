def is_palindrome(word):
    word = word.lower().replace(" ", "")  # Convert the word to lowercase and remove spaces
    return word == word[::-1]

word1 = "madam"
word2 = "hello"
word3 = "A man a plan a canal Panama"

print(f"'{word1}' is a palindrome: {is_palindrome(word1)}")
print(f"'{word2}' is a palindrome: {is_palindrome(word2)}")
print(f"'{word3}' is a palindrome: {is_palindrome(word3)}")