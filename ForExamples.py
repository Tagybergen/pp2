#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#2
for x in "banana":
  print(x)
#3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#5
for x in range(2, 30, 3):
  print(x)
#6
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
