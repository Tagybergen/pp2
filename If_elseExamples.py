#1
a = 33
b = 200
if b > a:
  print("b is greater than a")
#2
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#3
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#4
if a > b: print("a is greater than b")
#5
a = 2
b = 330
print("A") if a > b else print("B")
#6
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#7
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#8
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")  
#9
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#10
a = 33
b = 200

if b > a:
  pass