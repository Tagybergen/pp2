import re
text = "hello, world. This is a test"
new_text = re.sub(r'[ ,.]', ':', text)
print(new_text)
